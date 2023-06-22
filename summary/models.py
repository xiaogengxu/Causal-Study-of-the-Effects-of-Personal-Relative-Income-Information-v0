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

import csv

author = 'Your name here'

doc = """
Summary & Thank you
"""


class Constants(BaseConstants):
    name_in_url = 'summary'
    players_per_group = 200
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
