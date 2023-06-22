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
import json
from django.contrib.admin.utils import flatten

author = 'Your name here'

doc = """
Political preferences
"""


class Constants(BaseConstants):
    name_in_url = 'political_pref'
    players_per_group = 200
    num_rounds = 1

    trust_list = ['gov', 'union', 'politician']
    migration_trade_list = ['migration', 'trade']
    migration_list = ['migration_human', 'migration_work']
    redistribution_list = ['min_income', 'income_tax', 'inheritance_tax', 'redistribution', 'tax_burden']
    labor_market_list = ['unemployment', 'basic_income']


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            trust_seq = Constants.trust_list.copy()
            migration_trade_seq = Constants.migration_trade_list.copy()
            migration_seq = Constants.migration_list.copy()
            redistribution_seq = Constants.redistribution_list.copy()
            labor_market_seq = Constants.labor_market_list.copy()

            random.shuffle(trust_seq)
            random.shuffle(migration_trade_seq)
            random.shuffle(migration_seq)
            random.shuffle(redistribution_seq)
            random.shuffle(labor_market_seq)

            player.trust_seq0 = trust_seq[0]
            player.trust_seq1 = trust_seq[1]
            player.trust_seq2 = trust_seq[2]

            player.migration_trade_seq0 = migration_trade_seq[0]
            player.migration_trade_seq1 = migration_trade_seq[1]

            player.migration_seq0 = migration_seq[0]
            player.migration_seq1 = migration_seq[1]

            player.redistribution_seq0 = redistribution_seq[0]
            player.redistribution_seq1 = redistribution_seq[1]
            player.redistribution_seq2 = redistribution_seq[2]
            player.redistribution_seq3 = redistribution_seq[3]
            player.redistribution_seq4 = redistribution_seq[4]

            player.labor_market_seq0 = labor_market_seq[0]
            player.labor_market_seq1 = labor_market_seq[1]

        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
            pg_Gini1, pg_Gini2, pg_Redistribution, *tail = pb
            # Pack the two distribution choice questions together
            Gini_seq = [pg_Gini1, pg_Gini2]
            # Randomize the order of two distribution questions
            random.shuffle(Gini_seq)
            # Pack the distribution qs and Redistribution q
            Gini_Redistribution_seq = [Gini_seq, pg_Redistribution]
            # Randomize the order between two distribution qs and Redistribution
            random.shuffle(Gini_Redistribution_seq)
            # Flatten Gini_Redistribution_seq to a simple list
            Gini_Redistribution_seq1 = flatten(Gini_Redistribution_seq)
            pb1 = [Gini_Redistribution_seq1, *tail]
            # Shuffle the pack with other pages
            random.shuffle(pb1)
            # Flatten the list to one simple list
            pb = flatten(pb1)
            p.page_sequence = json.dumps(pb)
            p.participant.vars['ind_Gini1'] = pb.index('Gini1')
            p.participant.vars['ind_Gini2'] = pb.index('Gini2')
            p.participant.vars['ind_Redistribution'] = pb.index('Redistribution')
            p.participant.vars['ind_Trust'] = pb.index('Trust')
            p.participant.vars['ind_Migration_trade'] = pb.index('Migration_trade')
            p.participant.vars['ind_Labor_market'] = pb.index('Labor_market')


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    page_sequence = models.StringField()

    distribution1 = models.StringField(blank=True)
    distribution2 = models.StringField(blank=True)

    min_income = models.IntegerField(
        blank=True
    )

    income_tax = models.IntegerField()
    check_income_tax = models.IntegerField(blank=True)

    inheritance_tax = models.IntegerField()
    check_inheritance_tax = models.IntegerField(blank=True)

    redistribution = models.IntegerField()
    check_slider_redistribute = models.IntegerField(blank=True)

    tax_burden = models.IntegerField()
    check_slider_tax_burden = models.IntegerField(blank=True)

    redistribution_seq0 = models.StringField()
    redistribution_seq1 = models.StringField()
    redistribution_seq2 = models.StringField()
    redistribution_seq3 = models.StringField()
    redistribution_seq4 = models.StringField()

    trust_government = models.IntegerField()
    trust_union = models.IntegerField()
    trust_politician = models.IntegerField()

    check_slider_gov = models.IntegerField(blank=True)
    check_slider_union = models.IntegerField(blank=True)
    check_slider_politician = models.IntegerField(blank=True)

    trust_seq0 = models.StringField()
    trust_seq1 = models.StringField()
    trust_seq2 = models.StringField()

    migration_human = models.IntegerField()
    check_migration1 = models.IntegerField(blank=True)

    migration_work = models.IntegerField()
    check_migration2 = models.IntegerField(blank=True)

    trade = models.IntegerField(blank=True)
    check_trade = models.IntegerField(blank=True)

    migration_trade_seq0 = models.StringField()
    migration_trade_seq1 = models.StringField()

    migration_seq0 = models.StringField()
    migration_seq1 = models.StringField()

    unemployment = models.IntegerField()
    check_unemployment = models.IntegerField(blank=True)

    basic_income = models.IntegerField()
    check_basic_income = models.IntegerField(blank=True)

    labor_market_seq0 = models.StringField()
    labor_market_seq1 = models.StringField()

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
