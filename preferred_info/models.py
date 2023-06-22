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

# from otree_tools.models import fields as tool_models
from django import forms

import random

author = 'Your name here'

doc = """
Preferred information
"""


class Constants(BaseConstants):
    name_in_url = 'preferred_info'
    players_per_group = 200
    num_rounds = 1

    options = [('postcode',
                _('my income relative to those adults (18 years or older) who lived in the same municipality')),
               ('education', _('my income relative to those who had the same level of education')),
               ('occupation', _('my income relative to those who had the same occupation')),
               ('age', _('my income relative to those who are born in the same year')),
               ('all', _('my income relative to all adult (18 yrs or older) Finns'))]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # shuffle the options
            option_seq = Constants.options.copy()
            random.shuffle(option_seq)
            player.participant.vars['option_seq'] = option_seq
            # store the sequence
            player.option_seq0 = option_seq[0][0]
            player.option_seq1 = option_seq[1][0]
            player.option_seq2 = option_seq[2][0]
            player.option_seq3 = option_seq[3][0]
            player.option_seq4 = option_seq[4][0]


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    preferred_group = models.StringField(
        label="",
        choices=(),
        widget=widgets.RadioSelect,
        blank=True
    )

    option_seq0 = models.StringField(blank=True)
    option_seq1 = models.StringField(blank=True)
    option_seq2 = models.StringField(blank=True)
    option_seq3 = models.StringField(blank=True)
    option_seq4 = models.StringField(blank=True)

    specify_reason = models.LongStringField(
        label="",
        max_length=200,
        blank=True,
    )

    choice_reason = models.StringField(
        choices=(),
        label="",
        widget=forms.widgets.CheckboxSelectMultiple(
            choices=[('useful', _('I expect to use this information.')),
                     ('curious', _('I knew relatively little about my position in this group.')),
                     ('hard_to_find', _('This piece of information is difficult to find elsewhere.')),
                     ('important', _('This piece of information is most important to me.')),
                     ('high_belief', _('I expected my income to be relatively high and wanted to check '
                                       'whether it holds true.')),
                     ('low_belief', _('I expected my income to be relatively low and wanted to check '
                                      'whether it holds true.')),
                     ('not_interested', _('I am not interested in comparing my income to others\' incomes.')),
                     ('info_incorrect', _('Some information in the registers was incorrect, which affected my choice.')),
                     ('other', _('Some other reason, what?'))
                     ]),
        blank=True
    )
    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
