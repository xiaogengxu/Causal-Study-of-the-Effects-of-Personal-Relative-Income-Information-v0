from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Self_assessment(Page):
    form_model = 'player'
    form_fields = ['positive_reciprocity', 'negative_reciprocity', 'trust',
                   'competitiveness1', 'competitiveness2',
                   'check_slider1', 'check_slider2', 'check_slider3', 'check_slider4', 'check_slider5']

    def vars_for_template(self):
        condition = self.participant.vars['condition']
        social_seq0 = self.player.social_seq0
        social_seq1 = self.player.social_seq1
        social_seq2 = self.player.social_seq2
        social_seq3 = self.player.social_seq3
        social_seq4 = self.player.social_seq4

        return {"condition": condition,
                "social_seq0": social_seq0,
                "social_seq1": social_seq1,
                "social_seq2": social_seq2,
                "social_seq3": social_seq3,
                "social_seq4": social_seq4}

    def error_message(self, values):
        if not values['check_slider1'] or not values['check_slider2'] or not values['check_slider3'] or \
                not values['check_slider4'] or not values['check_slider5']:
            return _('Please answer all questions on this page.')


class Willingness_to_act(Page):
    form_model = 'player'
    form_fields = ['patience', 'altruism', 'risk_taking',
                   'check_slider6', 'check_slider7', 'check_slider8']

    def vars_for_template(self):
        condition = self.participant.vars['condition']
        act_seq0 = self.player.act_seq0
        act_seq1 = self.player.act_seq1
        act_seq2 = self.player.act_seq2

        return {"condition": condition,
                "act_seq0": act_seq0,
                "act_seq1": act_seq1,
                "act_seq2": act_seq2}

    def error_message(self, values):
        if not values['check_slider6'] or not values['check_slider7'] or not values['check_slider8']:
            return _('Please answer all questions on this page.')


class Political_orientation(Page):
    form_model = 'player'
    form_fields = ['political_right', 'check_political_right', 'political_liberal',
                   'check_political_liberal', 'party']

    def error_message(self, values):
        if not values['check_political_right'] or not values['check_political_liberal'] or \
                not values['party']:
            return _('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        return {"condition": condition,
                "app1": app1,
                "app2": app2,
                "app3": app3}


page_sequence = [Self_assessment, Willingness_to_act, Political_orientation]
