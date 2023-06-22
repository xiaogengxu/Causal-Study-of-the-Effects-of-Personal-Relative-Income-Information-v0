from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page as Page
from django.utils.translation import ugettext_lazy as _
import csv


class Background(Page):
    form_model = "player"
    form_fields = ['age', 'gender', 'live_with', 'occupation_2018', 'education_2018',
                   'municipality_2018']

    def error_message(self, values):
        if not values['age'] or not values['gender'] or not values['live_with'] or not values['occupation_2018'] or \
                not values['education_2018'] or not values['municipality_2018']:
            return _('Please answer all questions on this page.')

    def before_next_page(self):
        if self.player.education_2018 == 'basic':
            self.participant.vars['education_2018'] = _('Lower secondary education')
        if self.player.education_2018 == 'upper_secondary':
            self.participant.vars['education_2018'] = _('Upper secondary level education')
        if self.player.education_2018 == 'bachelor':
            self.participant.vars['education_2018'] = _('Bachelor\'s or equivalent level')
        elif self.player.education_2018 == 'master':
            self.participant.vars['education_2018'] = _('Master\'s or equivalent level or doctoral level')

        with open('stimuli_simulated_main.csv', 'r', encoding='UTF-8', newline='') as csv_data_set:
            data_set = csv.reader(csv_data_set)
            for row in data_set:
                if row[0] == self.participant.label:
                    self.participant.vars['occupation_fi'] = row[3]
                    self.participant.vars['occupation_sv'] = row[4]
                    if row[1] == '1':
                        self.participant.vars['condition'] = 'control'
                    if row[1] == '2':
                        self.participant.vars['condition'] = 'assigned'
                        self.participant.vars['treatment_assigned'] = 'education'
                        self.participant.vars['true_position'] = int(row[9])
                    if row[1] == '3':
                        self.participant.vars['condition'] = 'assigned'
                        self.participant.vars['treatment_assigned'] = 'occupation'
                        self.participant.vars['true_position'] = int(row[8])
                    if row[1] == '4':
                        self.participant.vars['condition'] = 'assigned'
                        self.participant.vars['treatment_assigned'] = 'postcode'
                        self.participant.vars['true_position'] = int(row[5])
                    if row[1] == '5':
                        self.participant.vars['condition'] = 'assigned'
                        self.participant.vars['treatment_assigned'] = 'age'
                        self.participant.vars['true_position'] = int(row[7])
                    if row[1] == '6':
                        self.participant.vars['condition'] = 'assigned'
                        self.participant.vars['treatment_assigned'] = 'all'
                        self.participant.vars['true_position'] = int(row[6])
                    if row[1] == '7':
                        self.participant.vars['condition'] = 'choice'
        csv_data_set.close()


page_sequence = [Background]
