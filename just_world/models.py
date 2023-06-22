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
Just world beliefs
"""


class Constants(BaseConstants):
    name_in_url = 'jwb'
    players_per_group = 200
    num_rounds = 1

    que_list1 = ['outcome', 'procedure']
    que_list2 = ['procedure_edu', 'procedure_job']


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            que_seq1 = Constants.que_list1.copy()
            que_seq2 = Constants.que_list2.copy()

            random.shuffle(que_seq1)
            random.shuffle(que_seq2)

            player.que_seq1_0 = que_seq1[0]
            player.que_seq1_1 = que_seq1[1]
            player.que_seq2_0 = que_seq2[0]
            player.que_seq2_1 = que_seq2[1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    outcome = models.IntegerField()
    procedure_edu = models.IntegerField()
    procedure_job = models.IntegerField()

    que_seq1_0 = models.StringField()
    que_seq1_1 = models.StringField()
    que_seq2_0 = models.StringField()
    que_seq2_1 = models.StringField()

    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3 = models.IntegerField(blank=True)

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
