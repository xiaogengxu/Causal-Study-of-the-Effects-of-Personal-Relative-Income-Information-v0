from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import datetime, json, time
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _
import csv


class Beliefs_nouislider(Page):
    form_model = "player"
    form_fields = ['s_postcode', 's_occupation', 's_education', 's_age', 's_all',
                   'check_slider1', 'check_slider2', 'check_slider3', 'check_slider4', 'check_slider5']

    def error_message(self, values):
        if not values['check_slider1'] or not values['check_slider2'] or not values['check_slider3'] or \
                not values['check_slider4'] or not values['check_slider5']:
            return _('Please answer all questions on this page.')

    def before_next_page(self):
        self.participant.vars['belief_postcode'] = self.player.s_postcode
        self.participant.vars['belief_occupation'] = self.player.s_occupation
        self.participant.vars['belief_education'] = self.player.s_education
        self.participant.vars['belief_age'] = self.player.s_age
        self.participant.vars['belief_all'] = self.player.s_all

    def vars_for_template(self):
        condition = self.participant.vars['condition']
        seq0 = self.player.seq0
        seq1 = self.player.seq1
        seq2 = self.player.seq2
        seq3 = self.player.seq3
        seq4 = self.player.seq4

        education_2018 = self.participant.vars['education_2018']

        occupation_fi = self.participant.vars['occupation_fi']
        occupation_sv = self.participant.vars['occupation_sv']

        incentive = self.participant.vars['incentive']

        return {"condition": condition,
                "seq0": seq0,
                "seq1": seq1,
                "seq2": seq2,
                "seq3": seq3,
                "seq4": seq4,
                "education_2018": education_2018,
                "occupation_fi": occupation_fi,
                "occupation_sv": occupation_sv,
                "incentive": incentive}


page_sequence = [Beliefs_nouislider]
