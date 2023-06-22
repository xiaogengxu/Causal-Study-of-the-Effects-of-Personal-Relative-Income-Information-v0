from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _

import random

author = 'Your name here'

doc = """
Belief elicitation
"""


class Constants(BaseConstants):
    name_in_url = 'beliefs'
    players_per_group = 200
    num_rounds = 1

    question_list = ['postcode', 'occupation', 'education', 'all', 'age']


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # randomize to treatment: control or assigned or choice reference group
            question_list_copy = Constants.question_list.copy()
            payoff_question = random.choice(question_list_copy)

            show_sequence = Constants.question_list.copy()
            random.shuffle(show_sequence)

            player.participant.vars['payoff_question'] = payoff_question
            player.payoff_question = payoff_question

            player.seq0 = show_sequence[0]
            player.seq1 = show_sequence[1]
            player.seq2 = show_sequence[2]
            player.seq3 = show_sequence[3]
            player.seq4 = show_sequence[4]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payoff_question = models.StringField()

    s_postcode = models.IntegerField()
    s_occupation = models.IntegerField()
    s_education = models.IntegerField()
    s_age = models.IntegerField()
    s_all = models.IntegerField()

    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3 = models.IntegerField(blank=True)
    check_slider4 = models.IntegerField(blank=True)
    check_slider5 = models.IntegerField(blank=True)

    seq0 = models.StringField()
    seq1 = models.StringField()
    seq2 = models.StringField()
    seq3 = models.StringField()
    seq4 = models.StringField()

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
