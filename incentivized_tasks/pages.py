from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import datetime, json, time
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Reminder_choice(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['condition'] == 'choice'

    def vars_for_template(self):
        if self.participant.vars['group_choice'] == 'postcode':
            stimuli_group = _('those who lived in the same municipality')
            preferred_group_choice1 = _('people who lived in the same municipality')
            belief = self.participant.vars['belief_postcode']
        elif self.participant.vars['group_choice'] == 'education':
            stimuli_group = _('those who had the same level of education')
            preferred_group_choice1 = _('people who had the same level of education')
            belief = self.participant.vars['belief_education']
        elif self.participant.vars['group_choice'] == 'occupation':
            stimuli_group = _('those who had the same occupation')
            preferred_group_choice1 = _('people who had the same occupation')
            belief = self.participant.vars['belief_occupation']
        elif self.participant.vars['group_choice'] == 'age':
            stimuli_group = _('those who are born in the same year')
            preferred_group_choice1 = _('people who are born in the same year as you')
            belief = self.participant.vars['belief_age']
        elif self.participant.vars['group_choice'] == 'all':
            stimuli_group = _('all Finns')
            preferred_group_choice1 = _('all other Finns')
            belief = self.participant.vars['belief_all']

        true_position = self.participant.vars['true_position']

        start_list = []

        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['incentive']

        return {"stimuli_group": stimuli_group,
                "preferred_group_choice1": preferred_group_choice1,
                "true_position": true_position,
                "belief": belief,
                "start_list": start_list,
                "incentive": incentive}


class Reminder_assigned(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['condition'] == 'assigned'

    def vars_for_template(self):
        if self.participant.vars['treatment_assigned'] == 'postcode':
            stimuli_group = _('those who lived in the same municipality')
            assigned_group1 = _('people who lived in the same municipality')
            belief = self.participant.vars['belief_postcode']
        elif self.participant.vars['treatment_assigned'] == 'education':
            stimuli_group = _('those who had the same level of education')
            assigned_group1 = _('people who had the same level of education')
            belief = self.participant.vars['belief_education']
        elif self.participant.vars['treatment_assigned'] == 'occupation':
            stimuli_group = _('those who had the same occupation')
            assigned_group1 = _('people who had the same occupation')
            belief = self.participant.vars['belief_occupation']
        elif self.participant.vars['treatment_assigned'] == 'age':
            stimuli_group = _('those who are born in the same year')
            assigned_group1 = _('people who are born in the same year as you')
            belief = self.participant.vars['belief_age']
        elif self.participant.vars['treatment_assigned'] == 'all':
            stimuli_group = _('all Finns')
            assigned_group1 = _('all other Finns')
            belief = self.participant.vars['belief_all']

        true_position = self.participant.vars['true_position']

        start_list = []

        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['incentive']

        return {"stimuli_group": stimuli_group,
                "assigned_group1": assigned_group1,
                "true_position": true_position,
                "belief": belief,
                "start_list": start_list,
                "incentive": incentive}


class Intro_incentive1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 1


class Intro_incentive0(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 0


class Incentive(Page):
    form_model = 'player'
    form_fields = ['donate', 'lotto', 'tax', 'check_slider_donate', 'check_slider_lotto', 'check_slider_tax']

    def error_message(self, values):
        if not values['check_slider_donate'] or not values['check_slider_lotto'] or not values['check_slider_tax']:
            return _('Please answer all questions on this page.')

    def vars_for_template(self):
        incentive_seq0 = self.player.incentive_seq0
        incentive_seq1 = self.player.incentive_seq1
        incentive_seq2 = self.player.incentive_seq2
        incentive = self.participant.vars['incentive']

        return {"incentive_seq0": incentive_seq0,
                "incentive_seq1": incentive_seq1,
                "incentive_seq2": incentive_seq2,
                "incentive": incentive}

    def before_next_page(self):
        self.participant.vars['donate'] = self.player.donate
        self.participant.vars['lotto'] = self.player.lotto
        self.participant.vars['tax'] = self.player.tax


class Draw_incentive(Page):
    form_model = 'player'
    form_fields = ['drawn_incentive', 'finished']

    def is_displayed(self):
        return self.participant.vars['incentive'] == 1

    def error_message(self, values):
        if not values['drawn_incentive']:
            return _('Please answer all questions on this page.')

    def before_next_page(self):
        end_datetime = datetime.datetime.now()
        start_time = self.participant.vars['start_time']
        self.player.total_time = round((end_datetime - start_time).total_seconds())
        self.participant.vars['drawn_incentive'] = self.player.drawn_incentive


page_sequence = [Reminder_choice, Reminder_assigned, Intro_incentive1, Intro_incentive0, Incentive, Draw_incentive]
