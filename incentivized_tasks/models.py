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
import csv

author = 'Your name here'

doc = """
Incentivized tasks
"""


class Constants(BaseConstants):
    name_in_url = 'tasks'
    players_per_group = 200
    num_rounds = 1
    incentive_list = ['donate', 'lotto', 'tax']


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            incentive_seq = Constants.incentive_list.copy()
            random.shuffle(incentive_seq)

            player.incentive_seq0 = incentive_seq[0]
            player.incentive_seq1 = incentive_seq[1]
            player.incentive_seq2 = incentive_seq[2]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donate = models.IntegerField()
    lotto = models.IntegerField()
    tax = models.IntegerField()

    check_slider_donate = models.IntegerField(blank=True)
    check_slider_lotto = models.IntegerField(blank=True)
    check_slider_tax = models.IntegerField(blank=True)

    incentive_seq0 = models.StringField()
    incentive_seq1 = models.StringField()
    incentive_seq2 = models.StringField()

    finished = models.IntegerField(blank=True)

    drawn_incentive = models.StringField(blank=True)

    total_time = models.IntegerField()

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
