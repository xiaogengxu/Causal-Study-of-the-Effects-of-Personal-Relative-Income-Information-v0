from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import datetime, json, time
import csv
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _
import math


class Summary_choice(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 1 and self.participant.vars['condition'] == 'choice'

    def vars_for_template(self):
        if self.participant.vars['payoff_question'] == 'postcode':
            group = _('those who lived in the same municipality')
            belief_bonus = self.participant.vars['belief_postcode']
            group_bonus = 'postcode'
        elif self.participant.vars['payoff_question'] == 'education':
            group = _('those who had the same level of education')
            belief_bonus = self.participant.vars['belief_education']
            group_bonus = 'education'
        elif self.participant.vars['payoff_question'] == 'occupation':
            group = _('those who had the same occupation')
            belief_bonus = self.participant.vars['belief_occupation']
            group_bonus = 'occupation'
        elif self.participant.vars['payoff_question'] == 'age':
            group = _('those who are born in the same year')
            belief_bonus = self.participant.vars['belief_age']
            group_bonus = 'age'
        elif self.participant.vars['payoff_question'] == 'all':
            group = _('all Finns')
            belief_bonus = self.participant.vars['belief_all']
            group_bonus = 'all'

        with open('stimuli_simulated_main.csv', 'r', encoding='UTF-8', newline='') as csv_data_set:
            data_set = csv.reader(csv_data_set)
            for row in data_set:
                if row[0] == self.participant.label:
                    if group_bonus == 'postcode':
                        belief_correct = int(row[5])
                    if group_bonus == 'education':
                        belief_correct = int(row[9])
                    if group_bonus == 'occupation':
                        belief_correct = int(row[8])
                    if group_bonus == 'age':
                        belief_correct = int(row[7])
                    elif group_bonus == 'all':
                        belief_correct = int(row[6])
        csv_data_set.close()

        def myfun(a):
            if a <= 5:
                l = 0
                h = 5
            if a > 5 and (a % 5 == 3 or a % 5 == 4 or a % 5 == 0):
                h = 5 * round(a / 5)
                l = h - 4
            if a > 5 and (a % 5 == 1 or a % 5 == 2):
                l = 5 * round(a / 5) + 1
                h = l + 4
            return [l, h]

        correct_list = myfun(belief_correct)

        if correct_list[0] <= belief_bonus <= correct_list[1]:
            correctness = _('Your assessment hits the correct 5%-point interval '
                            'and thus you will receive 5 euros in addition.')
            extra_pay = 5
        else:
            correctness = _('Your assessment does not hit the correct 5%-point interval '
                            'and thus you will not receive 5 euros in addition.')
            extra_pay = 0

        if self.participant.vars['group_choice'] == 'postcode':
            belief = self.participant.vars['belief_postcode']
        elif self.participant.vars['group_choice'] == 'education':
            belief = self.participant.vars['belief_education']
        elif self.participant.vars['group_choice'] == 'occupation':
            belief = self.participant.vars['belief_occupation']
        elif self.participant.vars['group_choice'] == 'age':
            belief = self.participant.vars['belief_age']
        elif self.participant.vars['group_choice'] == 'all':
            belief = self.participant.vars['belief_all']

        true_position = self.participant.vars['true_position']

        start_list = []

        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['drawn_incentive']

        if self.participant.vars['drawn_incentive'] in ['CHARITY', 'HYVÄNTEKEVÄISYYS', 'VÄLGÖRENHET']:
            incentive_pay = self.participant.vars['donate']
            total_pay = 15 - int(self.participant.vars['donate']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''
        elif self.participant.vars['drawn_incentive'] == 'LOTTO':
            incentive_pay = self.participant.vars['lotto']
            total_pay = 15 - int(self.participant.vars['lotto']) + extra_pay
            total_pay_txt1 = _(', and Lotto lottery tickets for ')
            total_pay_txt2 = _(' euros by mail')
            incentive_pay_lotto = self.participant.vars['lotto']
        elif self.participant.vars['drawn_incentive'] in ['TAX', 'VERO', 'SKATT']:
            incentive_pay = self.participant.vars['tax']
            total_pay = 15 - int(self.participant.vars['tax']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''

        if_incentive = self.participant.vars['incentive']

        return {"group": group,
                "correctness": correctness,
                "true_position": true_position,
                "belief": belief,
                "start_list": start_list,
                "incentive": incentive,
                "incentive_pay": incentive_pay,
                "belief_correct": belief_correct,
                "belief_bonus": belief_bonus,
                "total_pay": total_pay,
                "total_pay_txt1": total_pay_txt1,
                "total_pay_txt2": total_pay_txt2,
                "incentive_pay_lotto": incentive_pay_lotto,
                "if_incentive": if_incentive}

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://link.webropolsurveys.com/S/317743602C11ED39/?q1='+username_value)


class Summary_assigned(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 1 and self.participant.vars['condition'] == 'assigned'

    def vars_for_template(self):
        if self.participant.vars['payoff_question'] == 'postcode':
            group = _('those who lived in the same municipality')
            belief_bonus = self.participant.vars['belief_postcode']
            group_bonus = 'postcode'
        elif self.participant.vars['payoff_question'] == 'education':
            group = _('those who had the same level of education')
            belief_bonus = self.participant.vars['belief_education']
            group_bonus = 'education'
        elif self.participant.vars['payoff_question'] == 'occupation':
            group = _('those who had the same occupation')
            belief_bonus = self.participant.vars['belief_occupation']
            group_bonus = 'occupation'
        elif self.participant.vars['payoff_question'] == 'age':
            group = _('those who are born in the same year')
            belief_bonus = self.participant.vars['belief_age']
            group_bonus = 'age'
        elif self.participant.vars['payoff_question'] == 'all':
            group = _('all Finns')
            belief_bonus = self.participant.vars['belief_all']
            group_bonus = 'all'

        with open('stimuli_simulated_main.csv', 'r', encoding='UTF-8', newline='') as csv_data_set:
            data_set = csv.reader(csv_data_set)
            for row in data_set:
                if row[0] == self.participant.label:
                    if group_bonus == 'postcode':
                        belief_correct = int(row[5])
                    if group_bonus == 'education':
                        belief_correct = int(row[9])
                    if group_bonus == 'occupation':
                        belief_correct = int(row[8])
                    if group_bonus == 'age':
                        belief_correct = int(row[7])
                    elif group_bonus == 'all':
                        belief_correct = int(row[6])
        csv_data_set.close()

        def myfun(a):
            if a <= 5:
                l = 0
                h = 5
            if a > 5 and (a % 5 == 3 or a % 5 == 4 or a % 5 == 0):
                h = 5 * round(a / 5)
                l = h - 4
            if a > 5 and (a % 5 == 1 or a % 5 == 2):
                l = 5 * round(a / 5) + 1
                h = l + 4
            return [l, h]

        correct_list = myfun(belief_correct)

        if correct_list[0] <= belief_bonus <= correct_list[1]:
            correctness = _('Your assessment hits the correct 5%-point interval '
                            'and thus you will receive 5 euros in addition.')
            extra_pay = 5
        else:
            correctness = _('Your assessment does not hit the correct 5%-point interval '
                            'and thus you will not receive 5 euros in addition.')
            extra_pay = 0

        if self.participant.vars['treatment_assigned'] == 'postcode':
            belief = self.participant.vars['belief_postcode']
        elif self.participant.vars['treatment_assigned'] == 'education':
            belief = self.participant.vars['belief_education']
        elif self.participant.vars['treatment_assigned'] == 'occupation':
            belief = self.participant.vars['belief_occupation']
        elif self.participant.vars['treatment_assigned'] == 'age':
            belief = self.participant.vars['belief_age']
        elif self.participant.vars['treatment_assigned'] == 'all':
            belief = self.participant.vars['belief_all']

        true_position = self.participant.vars['true_position']

        start_list = []

        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['drawn_incentive']

        if self.participant.vars['drawn_incentive'] in ['CHARITY', 'HYVÄNTEKEVÄISYYS', 'VÄLGÖRENHET']:
            incentive_pay = self.participant.vars['donate']
            total_pay = 15 - int(self.participant.vars['donate']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''
        elif self.participant.vars['drawn_incentive'] == 'LOTTO':
            incentive_pay = self.participant.vars['lotto']
            total_pay = 15 - int(self.participant.vars['lotto']) + extra_pay
            total_pay_txt1 = _(', and Lotto lottery tickets for ')
            total_pay_txt2 = _(' euros by mail')
            incentive_pay_lotto = self.participant.vars['lotto']
        elif self.participant.vars['drawn_incentive'] in ['TAX', 'VERO', 'SKATT']:
            incentive_pay = self.participant.vars['tax']
            total_pay = 15 - int(self.participant.vars['tax']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''

        if_incentive = self.participant.vars['incentive']

        return {"group": group,
                "correctness": correctness,
                "true_position": true_position,
                "belief": belief,
                "start_list": start_list,
                "incentive": incentive,
                "incentive_pay": incentive_pay,
                "belief_correct": belief_correct,
                "belief_bonus": belief_bonus,
                "total_pay": total_pay,
                "total_pay_txt1": total_pay_txt1,
                "total_pay_txt2": total_pay_txt2,
                "incentive_pay_lotto": incentive_pay_lotto,
                "if_incentive": if_incentive}

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://link.webropolsurveys.com/S/317743602C11ED39/?q1='+username_value)


class Summary_control(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 1 and self.participant.vars['condition'] == 'control'

    def vars_for_template(self):
        if self.participant.vars['payoff_question'] == 'postcode':
            group = _('those who lived in the same municipality')
            belief_bonus = self.participant.vars['belief_postcode']
            group_bonus = 'postcode'
        elif self.participant.vars['payoff_question'] == 'education':
            group = _('those who had the same level of education')
            belief_bonus = self.participant.vars['belief_education']
            group_bonus = 'education'
        elif self.participant.vars['payoff_question'] == 'occupation':
            group = _('those who had the same occupation')
            belief_bonus = self.participant.vars['belief_occupation']
            group_bonus = 'occupation'
        elif self.participant.vars['payoff_question'] == 'age':
            group = _('those who are born in the same year')
            belief_bonus = self.participant.vars['belief_age']
            group_bonus = 'age'
        elif self.participant.vars['payoff_question'] == 'all':
            group = _('all Finns')
            belief_bonus = self.participant.vars['belief_all']
            group_bonus = 'all'

        with open('stimuli_simulated_main.csv', 'r', encoding='UTF-8', newline='') as csv_data_set:
            data_set = csv.reader(csv_data_set)
            for row in data_set:
                if row[0] == self.participant.label:
                    if group_bonus == 'postcode':
                        belief_correct = int(row[5])
                    if group_bonus == 'education':
                        belief_correct = int(row[9])
                    if group_bonus == 'occupation':
                        belief_correct = int(row[8])
                    if group_bonus == 'age':
                        belief_correct = int(row[7])
                    elif group_bonus == 'all':
                        belief_correct = int(row[6])
        csv_data_set.close()

        def myfun(a):
            if a <= 5:
                l = 0
                h = 5
            if a > 5 and (a % 5 == 3 or a % 5 == 4 or a % 5 == 0):
                h = 5 * round(a / 5)
                l = h - 4
            if a > 5 and (a % 5 == 1 or a % 5 == 2):
                l = 5 * round(a / 5) + 1
                h = l + 4
            return [l, h]

        correct_list = myfun(belief_correct)

        if correct_list[0] <= belief_bonus <= correct_list[1]:
            correctness = _('Your assessment hits the correct 5%-point interval '
                            'and thus you will receive 5 euros in addition.')
            extra_pay = 5
        else:
            correctness = _('Your assessment does not hit the correct 5%-point interval '
                            'and thus you will not receive 5 euros in addition.')
            extra_pay = 0

        incentive = self.participant.vars['drawn_incentive']

        if self.participant.vars['drawn_incentive'] in ['CHARITY', 'HYVÄNTEKEVÄISYYS', 'VÄLGÖRENHET']:
            incentive_pay = self.participant.vars['donate']
            total_pay = 15 - int(self.participant.vars['donate']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''
        elif self.participant.vars['drawn_incentive'] == 'LOTTO':
            incentive_pay = self.participant.vars['lotto']
            total_pay = 15 - int(self.participant.vars['lotto']) + extra_pay
            total_pay_txt1 = _(', and Lotto lottery tickets for ')
            total_pay_txt2 = _(' euros by mail')
            incentive_pay_lotto = self.participant.vars['lotto']
        elif self.participant.vars['drawn_incentive'] in ['TAX', 'VERO', 'SKATT']:
            incentive_pay = self.participant.vars['tax']
            total_pay = 15 - int(self.participant.vars['tax']) + extra_pay
            total_pay_txt1 = ''
            total_pay_txt2 = ''
            incentive_pay_lotto = ''

        if_incentive = self.participant.vars['incentive']

        return {"group": group,
                "correctness": correctness,
                "incentive": incentive,
                "incentive_pay": incentive_pay,
                "belief_correct": belief_correct,
                "belief_bonus": belief_bonus,
                "total_pay": total_pay,
                "total_pay_txt1": total_pay_txt1,
                "total_pay_txt2": total_pay_txt2,
                "incentive_pay_lotto": incentive_pay_lotto,
                "if_incentive": if_incentive}

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://link.webropolsurveys.com/S/317743602C11ED39/?q1='+username_value)


class Summary_noincentive(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.participant.vars['incentive'] == 0


page_sequence = [Summary_choice, Summary_assigned, Summary_control, Summary_noincentive]
