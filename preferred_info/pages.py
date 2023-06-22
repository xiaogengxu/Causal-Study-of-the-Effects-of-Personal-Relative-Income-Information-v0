from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _
import csv


class Preferred_info(Page):
    form_model = "player"
    form_fields = ["preferred_group"]

    def is_displayed(self):
        return self.participant.vars['condition'] == 'choice'

    def preferred_group_choices(self):
        options = self.participant.vars['option_seq']
        return options

    def error_message(self, values):
        if not values['preferred_group']:
            return _('Please choose one of the options.')

    def before_next_page(self):
        self.participant.vars['group_choice'] = self.player.preferred_group

        with open('stimuli_simulated_main.csv', 'r', encoding='UTF-8', newline='') as csv_data_set:
            data_set = csv.reader(csv_data_set)
            for row in data_set:
                if row[0] == self.participant.label:
                    if self.player.preferred_group == 'postcode':
                        self.participant.vars['true_position'] = int(row[5])
                    if self.player.preferred_group == 'education':
                        self.participant.vars['true_position'] = int(row[9])
                    if self.player.preferred_group == 'occupation':
                        self.participant.vars['true_position'] = int(row[8])
                    if self.player.preferred_group == 'age':
                        self.participant.vars['true_position'] = int(row[7])
                    if self.player.preferred_group == 'all':
                        self.participant.vars['true_position'] = int(row[6])
        csv_data_set.close()


class Choice_reason(Page):
    form_model = "player"
    form_fields = ["choice_reason", "specify_reason"]

    def is_displayed(self):
        return self.participant.vars['condition'] == 'choice'

    def vars_for_template(self):
        if self.participant.vars['group_choice'] == 'postcode':
            preferred_group_choice = _('those who lived in the same municipality')
        elif self.participant.vars['group_choice'] == 'education':
            preferred_group_choice = _('those who had the same level of education')
        elif self.participant.vars['group_choice'] == 'occupation':
            preferred_group_choice = _('those who had the same occupation')
        elif self.participant.vars['group_choice'] == 'age':
            preferred_group_choice = _('those who are born in the same year')
        else:
            preferred_group_choice = _('all Finns')

        return {"preferred_group_choice": preferred_group_choice}

    def error_message(self, values):
        if not values['choice_reason']:
            return _('Please answer all questions. You must check at least one of the options.')
        if values['choice_reason']:
            selected_list = values['choice_reason']
            if 'high_belief' in selected_list and 'low_belief' in selected_list:
                return _('Please check your answers in the multiple choice option. '
                         'There is a conflict between the alternatives you chose.')


page_sequence = [Preferred_info, Choice_reason]
