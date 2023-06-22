from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
# from ._builtin import Page as oTreePage
from .models import Constants
import datetime, json, time, csv
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Welcome(Page):
    form_model = 'player'
    form_fields = ['username', 'password', 'check_password']

    def before_next_page(self):
        start_datetime = datetime.datetime.now()
        self.participant.vars['start_time'] = start_datetime
        self.participant.label = self.player.username

    def error_message(self, values):
        user_dict = {}
        user_set = csv.reader(open('username_simulated_main_collection.csv'), delimiter=',')
        for row in user_set:
            if row[0] != 'username':
                user_dict.update({row[0]: row[1]})
        if values['username'] not in user_dict or not values['check_password']:
            return _('Your username or password is incorrect. '
                     'Please check the information in the invitation letter and input again.')

    def vars_for_template(self):
        user_dict = {}
        user_set = csv.reader(open('username_simulated_main_collection.csv'), delimiter=',')
        for row in user_set:
            if row[0] != 'username':
                user_dict.update({row[0]: row[1]})

        if self.participant.vars['incentive'] == 1:
            pay_txt = _('You can guarantee yourself a payment of 15 euros by completing the survey. ')
        else:
            pay_txt = ''

        return {'user_dict': user_dict,
                'pay_txt': pay_txt}


page_sequence = [Welcome]
