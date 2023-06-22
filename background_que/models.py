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

author = 'Your name here'

doc = """
Background questions
"""

list_age = list(range(1970, 1991, 1))


class Constants(BaseConstants):
    name_in_url = 'background_que'
    players_per_group = 200
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        choices=list_age,
        blank=True
    )
    gender = models.StringField(
        choices=[('male', _('Male')), ('female', _('Female')), ('non_binary', _('Non-binary (other)')),
                 ('no answer', _('Prefer not to answer'))],
        widget=widgets.RadioSelect,
        label=_('What is your gender?'),
        blank=True
    )
    live_with = models.StringField(
        choices=[('alone', _('I live alone')), ('spouse', _('Together with my spouse')),
                 ('spouse_child', _('I live with my spouse and child(ren)')),
                 ('alone_child', _('Alone with a child/children')),
                 ('other', _('Some other situation'))],
        widget=widgets.RadioSelect,
        label=_('Who do you currently live with?'),
        blank=True
    )
    occupation_2018 = models.StringField(
        label=_('What was your occupation (or mention if you were unemployed or not part of the labour force)? '
                'Please write your answer in the field below.'),
        blank=True
    )
    education_2018 = models.StringField(
        blank=True
    )
    municipality_2018 = models.StringField(
        label=_('Where did you live? Please write the name of your municipality of residence in the field below.'),
        blank=True
    )
    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
