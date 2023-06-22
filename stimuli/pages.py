from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Stimuli_choice(Page):
    form_model = "player"
    form_fields = ['confirm_info', 'check_confirm_info']

    def is_displayed(self):
        return self.participant.vars['condition'] == 'choice'

    def error_message(self, values):
        if not values['check_confirm_info']:
            return _('Please look again at the information on this page and revise your answer by choosing a statement '
                     'that reflects the information.')

    def vars_for_template(self):
        if self.participant.vars['group_choice'] == 'postcode':
            preferred_group_choice = _('those who lived in the same municipality')
            preferred_group_choice1 = _('people who lived in the same municipality')
            belief = self.participant.vars['belief_postcode']
        elif self.participant.vars['group_choice'] == 'education':
            preferred_group_choice = _('those who had the same level of education')
            preferred_group_choice1 = _('people who had the same level of education')
            belief = self.participant.vars['belief_education']
        elif self.participant.vars['group_choice'] == 'occupation':
            preferred_group_choice = _('those who had the same occupation')
            preferred_group_choice1 = _('people who had the same occupation')
            belief = self.participant.vars['belief_occupation']
        elif self.participant.vars['group_choice'] == 'age':
            preferred_group_choice = _('those who are born in the same year')
            preferred_group_choice1 = _('people who are born in the same year as you')
            belief = self.participant.vars['belief_age']
        elif self.participant.vars['group_choice'] == 'all':
            preferred_group_choice = _('all Finns')
            preferred_group_choice1 = _('all other Finns')
            belief = self.participant.vars['belief_all']

        true_position = self.participant.vars['true_position']

        start_list = []
        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['incentive']

        return {"preferred_group_choice": preferred_group_choice,
                "preferred_group_choice1": preferred_group_choice1,
                "belief": belief,
                "true_position": true_position,
                "start_list": start_list,
                "incentive": incentive}


class Stimuli_assigned(Page):
    form_model = "player"
    form_fields = ['confirm_info', 'check_confirm_info']

    def is_displayed(self):
        return self.participant.vars['condition'] == 'assigned'

    def error_message(self, values):
        if not values['check_confirm_info']:
            return _('Please look again at the information on this page and revise your answer by choosing a statement '
                     'that reflects the information.')

    def vars_for_template(self):
        if self.participant.vars['treatment_assigned'] == 'postcode':
            belief = self.participant.vars['belief_postcode']
            assigned_group = _('those who lived in the same municipality')
            assigned_group1 = _('people who lived in the same municipality')
        elif self.participant.vars['treatment_assigned'] == 'education':
            belief = self.participant.vars['belief_education']
            assigned_group = _('those who had the same level of education')
            assigned_group1 = _('people who had the same level of education')
        elif self.participant.vars['treatment_assigned'] == 'occupation':
            belief = self.participant.vars['belief_occupation']
            assigned_group = _('those who had the same occupation')
            assigned_group1 = _('people who had the same occupation')
        elif self.participant.vars['treatment_assigned'] == 'age':
            belief = self.participant.vars['belief_age']
            assigned_group = _('those who are born in the same year')
            assigned_group1 = _('people who are born in the same year as you')
        else:
            belief = self.participant.vars['belief_all']
            assigned_group = _('all Finns')
            assigned_group1 = _('all other Finns')

        true_position = self.participant.vars['true_position']

        start_list = []
        if belief >= true_position:
            start_list.extend([true_position, belief])
        else:
            start_list.extend([belief, true_position])

        incentive = self.participant.vars['incentive']

        return {"belief": belief,
                "assigned_group": assigned_group,
                "assigned_group1": assigned_group1,
                "true_position": true_position,
                "start_list": start_list,
                "incentive": incentive}


page_sequence = [Stimuli_choice, Stimuli_assigned]
