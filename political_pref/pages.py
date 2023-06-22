from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
# Use ugettext_lazy instead of _ because _ is used in randomizing pages
from django.utils.translation import ugettext_lazy
import json


class Gini1(Page):
    form_model = 'player'
    form_fields = ['distribution1']

    def error_message(self, values):
        if not values['distribution1']:
            return ugettext_lazy('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Gini1 = self.participant.vars['ind_Gini1']
        ind_Gini2 = self.participant.vars['ind_Gini2']

        return {"condition": condition,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Gini1": ind_Gini1,
                "ind_Gini2": ind_Gini2}


class Gini2(Page):
    form_model = 'player'
    form_fields = ['distribution2']

    def error_message(self, values):
        if not values['distribution2']:
            return ugettext_lazy('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Gini1 = self.participant.vars['ind_Gini1']
        ind_Gini2 = self.participant.vars['ind_Gini2']

        return {"condition": condition,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Gini1": ind_Gini1,
                "ind_Gini2": ind_Gini2}


class Redistribution(Page):
    form_model = 'player'
    form_fields = ['min_income', 'income_tax', 'check_income_tax', 'inheritance_tax', 'check_inheritance_tax',
                   'redistribution', 'check_slider_redistribute', 'tax_burden', 'check_slider_tax_burden']

    def error_message(self, values):
        if not values['check_income_tax'] or not values['check_inheritance_tax'] or \
                not values['check_slider_redistribute'] or not values['check_slider_tax_burden'] or \
                (not values['min_income'] and values['min_income'] != -0):
            return ugettext_lazy('Please answer all questions on this page.')
        if values['min_income']:
            if values['min_income'] == -0 or values['min_income'] < 0:
                return ugettext_lazy('Please write a sum that is larger than, or equal to 0.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        redistribution_seq0 = self.player.redistribution_seq0
        redistribution_seq1 = self.player.redistribution_seq1
        redistribution_seq2 = self.player.redistribution_seq2
        redistribution_seq3 = self.player.redistribution_seq3
        redistribution_seq4 = self.player.redistribution_seq4

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Redistribution = self.participant.vars['ind_Redistribution']

        return {"condition": condition,
                "redistribution_seq0": redistribution_seq0,
                "redistribution_seq1": redistribution_seq1,
                "redistribution_seq2": redistribution_seq2,
                "redistribution_seq3": redistribution_seq3,
                "redistribution_seq4": redistribution_seq4,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Redistribution": ind_Redistribution}


class Trust(Page):
    form_model = 'player'
    form_fields = ['trust_government', 'trust_union', 'trust_politician',
                   'check_slider_gov', 'check_slider_union', 'check_slider_politician']

    def error_message(self, values):
        if not values['check_slider_gov'] or not values['check_slider_union'] or \
                not values['check_slider_politician']:
            return ugettext_lazy('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        trust_seq0 = self.player.trust_seq0
        trust_seq1 = self.player.trust_seq1
        trust_seq2 = self.player.trust_seq2

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Trust = self.participant.vars['ind_Trust']

        return {"condition": condition,
                "trust_seq0": trust_seq0,
                "trust_seq1": trust_seq1,
                "trust_seq2": trust_seq2,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Trust": ind_Trust}


class Migration_trade(Page):
    form_model = 'player'
    form_fields = ['migration_human', 'check_migration1', 'migration_work', 'check_migration2', 'trade', 'check_trade']

    def error_message(self, values):
        if not values['check_migration1'] or not values['check_migration2'] or not values['check_trade']:
            return ugettext_lazy('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        migration_trade_seq0 = self.player.migration_trade_seq0
        migration_trade_seq1 = self.player.migration_trade_seq1
        migration_seq0 = self.player.migration_seq0
        migration_seq1 = self.player.migration_seq1

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Migration_trade = self.participant.vars['ind_Migration_trade']

        return {"condition": condition,
                "migration_trade_seq0": migration_trade_seq0,
                "migration_trade_seq1": migration_trade_seq1,
                "migration_seq0": migration_seq0,
                "migration_seq1": migration_seq1,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Migration_trade": ind_Migration_trade}


class Labor_market(Page):
    form_model = 'player'
    form_fields = ['unemployment', 'check_unemployment', 'basic_income', 'check_basic_income']

    def error_message(self, values):
        if not values['check_unemployment'] or not values['check_basic_income']:
            return ugettext_lazy('Please answer all questions on this page.')

    def vars_for_template(self):
        condition = self.participant.vars['condition']

        labor_market_seq0 = self.player.labor_market_seq0
        labor_market_seq1 = self.player.labor_market_seq1

        app1 = self.participant.vars['app1']
        app2 = self.participant.vars['app2']
        app3 = self.participant.vars['app3']

        ind_Labor_market = self.participant.vars['ind_Labor_market']

        return {"condition": condition,
                "labor_market_seq0": labor_market_seq0,
                "labor_market_seq1": labor_market_seq1,
                "app1": app1,
                "app2": app2,
                "app3": app3,
                "ind_Labor_market": ind_Labor_market}


initial_page_sequence = [Gini1, Gini2, Redistribution, Trust, Migration_trade, Labor_market]

page_sequence = []


class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])
