from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Fairness(Page):
    form_model = 'player'
    form_fields = ['outcome', 'procedure_edu', 'procedure_job',
                   'check_slider1', 'check_slider2', 'check_slider3']

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        que_seq1_0 = self.player.que_seq1_0
        que_seq1_1 = self.player.que_seq1_1
        que_seq2_0 = self.player.que_seq2_0
        que_seq2_1 = self.player.que_seq2_1

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        return {"condition": condition,
                "que_seq1_0": que_seq1_0,
                "que_seq1_1": que_seq1_1,
                "que_seq2_0": que_seq2_0,
                "que_seq2_1": que_seq2_1,
                "app1": app1,
                "app2": app2,
                "app3": app3}

    def error_message(self, values):
        if not values['check_slider1'] or not values['check_slider2'] or not values['check_slider3']:
            return _('Please answer all questions on this page.')


page_sequence = [Fairness]
