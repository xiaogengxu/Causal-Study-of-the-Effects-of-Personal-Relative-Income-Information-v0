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
Social preferences
"""


class Constants(BaseConstants):
    name_in_url = 'social_pref'
    players_per_group = 200
    num_rounds = 1

    que_list = ['posi_reci', 'neg_reci', 'trust_seq', 'compete1', 'compete2']
    que_list_act = ['patience_seq', 'altruism_seq', 'risk_taking_seq']


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            ques_seq = Constants.que_list.copy()
            random.shuffle(ques_seq)

            que_seq_act = Constants.que_list_act.copy()
            random.shuffle(que_seq_act)

            player.social_seq0 = ques_seq[0]
            player.social_seq1 = ques_seq[1]
            player.social_seq2 = ques_seq[2]
            player.social_seq3 = ques_seq[3]
            player.social_seq4 = ques_seq[4]

            player.act_seq0 = que_seq_act[0]
            player.act_seq1 = que_seq_act[1]
            player.act_seq2 = que_seq_act[2]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    positive_reciprocity = models.IntegerField()
    negative_reciprocity = models.IntegerField()
    trust = models.IntegerField()
    competitiveness1 = models.IntegerField()
    competitiveness2 = models.IntegerField()

    social_seq0 = models.StringField()
    social_seq1 = models.StringField()
    social_seq2 = models.StringField()
    social_seq3 = models.StringField()
    social_seq4 = models.StringField()

    patience = models.IntegerField()
    altruism = models.IntegerField()
    risk_taking = models.IntegerField()

    act_seq0 = models.StringField()
    act_seq1 = models.StringField()
    act_seq2 = models.StringField()

    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3 = models.IntegerField(blank=True)
    check_slider4 = models.IntegerField(blank=True)
    check_slider5 = models.IntegerField(blank=True)

    check_slider6 = models.IntegerField(blank=True)
    check_slider7 = models.IntegerField(blank=True)
    check_slider8 = models.IntegerField(blank=True)

    political_right = models.IntegerField()
    check_political_right = models.IntegerField(blank=True)

    political_liberal = models.IntegerField()
    check_political_liberal = models.IntegerField(blank=True)

    party = models.StringField(blank=True)

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
