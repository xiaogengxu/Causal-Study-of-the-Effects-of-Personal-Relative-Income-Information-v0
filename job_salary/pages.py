from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Life(Page):
    form_model = 'player'
    form_fields = ['life_satisfied', 'fair_income', 'disappointed_income',
                   'search_job', 'invest', 'gamble', 'if_employed', 'union_member',
                   'check_slider1', 'check_slider2', 'check_slider3_1']

    def before_next_page(self):
        self.participant.vars['employment'] = self.player.if_employed

    def vars_for_template(self):
        if self.participant.vars['condition'] == 'choice' and self.participant.vars['group_choice'] == 'postcode':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who lived in the same municipality in 2018.')
        elif self.participant.vars['condition'] == 'choice' and self.participant.vars['group_choice'] == 'education':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who had the same level of education in 2018.')
        elif self.participant.vars['condition'] == 'choice' and self.participant.vars['group_choice'] == 'occupation':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who had the same occupation in 2018.')
        elif self.participant.vars['condition'] == 'choice' and self.participant.vars['group_choice'] == 'age':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who are born in the same year in 2018.')
        elif self.participant.vars['condition'] == 'choice' and self.participant.vars['group_choice'] == 'all':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of all Finns in 2018.')

        if self.participant.vars['condition'] == 'assigned' and \
                self.participant.vars['treatment_assigned'] == 'postcode':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who lived in the same municipality in 2018.')
        elif self.participant.vars['condition'] == 'assigned' and \
                self.participant.vars['treatment_assigned'] == 'education':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who had the same level of education in 2018.')
        elif self.participant.vars['condition'] == 'assigned' and \
                self.participant.vars['treatment_assigned'] == 'occupation':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who had the same occupation in 2018.')
        elif self.participant.vars['condition'] == 'assigned' and \
                self.participant.vars['treatment_assigned'] == 'age':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of those who are born in the same year in 2018.')
        elif self.participant.vars['condition'] == 'assigned' and \
                self.participant.vars['treatment_assigned'] == 'all':
            relative_group = _('In a previous part, you saw information about the relationship between your income '
                               'and the incomes of all Finns in 2018.')

        if self.participant.vars['condition'] == 'control':
            relative_group = ''

        condition = self.participant.vars['condition']

        que_seq0 = self.player.que_seq0
        que_seq1 = self.player.que_seq1
        que_seq2 = self.player.que_seq2
        que_seq3 = self.player.que_seq3
        que_seq4 = self.player.que_seq4

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        return {"relative_group": relative_group,
                "condition": condition,
                "que_seq0": que_seq0,
                "que_seq1": que_seq1,
                "que_seq2": que_seq2,
                "que_seq3": que_seq3,
                "que_seq4": que_seq4,
                "app1": app1,
                "app2": app2,
                "app3": app3}

    def error_message(self, values):
        if not values['check_slider1'] or not values['check_slider2'] or not values['check_slider3_1'] or \
                not values['search_job'] or not values['invest'] or \
                not values['gamble'] or not values['if_employed'] or not values['union_member']:
            return _('Please answer all questions on this page.')


class Job(Page):
    form_model = 'player'
    form_fields = ['wage_satisfied', 'job_satisfied', 'meaningful', 'check_slider9a', 'check_slider9b',
                   'check_slider9c']

    def is_displayed(self):
        return (not self.player.if_employed == 'unemployed') and (not self.player.if_employed == 'not_in_labor')

    def error_message(self, values):
        if not values['check_slider9a'] or not values['check_slider9b'] or not values['check_slider9c']:
            return _('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']
        employment = self.participant.vars['employment']

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        return {"condition": condition,
                "employment": employment,
                "app1": app1,
                "app2": app2,
                "app3": app3}


page_sequence = [Life, Job]
