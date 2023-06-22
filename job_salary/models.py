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
from django.contrib.admin.utils import flatten

import random

author = 'Your name here'

doc = """
Life and job
"""


class Constants(BaseConstants):
    name_in_url = 'life&job'
    players_per_group = 200
    num_rounds = 1
    que_list1 = ['search_job', 'invest', 'gamble']
    que_list2 = ['life_satisfied', 'fairness_feeling', que_list1]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            que_sequence1 = Constants.que_list1.copy()
            que_sequence2 = Constants.que_list2.copy()

            random.shuffle(que_sequence1)
            random.shuffle(que_sequence2)

            que_sequence = flatten(que_sequence2)

            player.que_seq0 = que_sequence[0]
            player.que_seq1 = que_sequence[1]
            player.que_seq2 = que_sequence[2]
            player.que_seq3 = que_sequence[3]
            player.que_seq4 = que_sequence[4]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    life_satisfied = models.IntegerField()

    fair_income = models.IntegerField()

    disappointed_income = models.IntegerField()

    search_job = models.StringField(
        label=_('How likely is it that you will search for a new job in the next six months?'),
        choices=[('unlikely', _('Very unlikely')), ('bit_unlikely', _('Somewhat unlikely')),
                 ('bit_likely', _('Somewhat likely')), ('likely', _('Very likely'))],
        widget=widgets.RadioSelect,
        blank=True
    )

    invest = models.StringField(
        label=_('How likely is it that you will buy or sell stocks or assets '
                '(excluding the house you are living right now) during the next six months?'),
        choices=[('unlikely', _('Very unlikely')), ('bit_unlikely', _('Somewhat unlikely')),
                 ('bit_likely', _('Somewhat likely')), ('likely', _('Very likely'))],
        widget=widgets.RadioSelect,
        blank=True
    )

    gamble = models.StringField(
        label=_('How likely is it that you will engage in gambling activities provided by Veikkaus during the next '
                'six months? By gambling activities, we mean for example buying tickets for the weekly national Lotto, '
                'playing slot machines and sports betting.'),
        choices=[('unlikely', _('Very unlikely')), ('bit_unlikely', _('Somewhat unlikely')),
                 ('bit_likely', _('Somewhat likely')), ('likely', _('Very likely'))],
        widget=widgets.RadioSelect,
        blank=True
    )

    if_employed = models.StringField(
        blank=True
    )

    union_member = models.IntegerField(
        label=_('Are you a member of any labor union or unemployment fund?'),
        choices=[(1, _('Yes')), (2, _('No'))],
        widget=widgets.RadioSelect,
        blank=True
    )

    que_seq0 = models.StringField()
    que_seq1 = models.StringField()
    que_seq2 = models.StringField()
    que_seq3 = models.StringField()
    que_seq4 = models.StringField()

    wage_satisfied = models.IntegerField()
    job_satisfied = models.IntegerField()
    meaningful = models.IntegerField()

    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3_1 = models.IntegerField(blank=True)

    check_slider9a = models.IntegerField(blank=True)
    check_slider9b = models.IntegerField(blank=True)
    check_slider9c = models.IntegerField(blank=True)

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
