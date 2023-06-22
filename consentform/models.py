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
import csv
import random
import json

from django.utils.translation import ugettext_lazy as _

author = 'Your name here'

doc = """
Informed consent
"""


def seq_to_dict(s):
    r = {}
    l = len(s) - 1
    for i, j in enumerate(s):
        if i < l:
            r[j] = s[i + 1]
        else:
            r[j] = None
    return r


class Constants(BaseConstants):
    name_in_url = 'welcome'
    players_per_group = 200
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.session.config['name'] == 'Relative_income':
            for player in self.get_players():
                player.participant.vars['incentive'] = 1
        else:
            for player in self.get_players():
                player.participant.vars['incentive'] = 0

        app_seq = self.session.config.get('app_sequence')
        for p in self.get_players():
            app_consent, app_background, app_beliefs, app_preferred_info, app_stimuli, app_job_salary, \
                app_just_world, app_political_pref, app_social_pref, app_incentivized_tasks, app_summary = app_seq
            head_apps = [app_consent, app_background, app_beliefs, app_preferred_info, app_stimuli]
            tail_apps = [app_social_pref, app_incentivized_tasks, app_summary]
            rdm_apps = [app_job_salary, app_just_world, app_political_pref]
            random.shuffle(rdm_apps)
            new_app_seq = head_apps + rdm_apps + tail_apps
            p.apps_show1 = new_app_seq[5]
            p.apps_show2 = new_app_seq[6]
            p.apps_show3 = new_app_seq[7]
            p.participant.vars['app1'] = new_app_seq[5]
            p.participant.vars['app2'] = new_app_seq[6]
            p.participant.vars['app3'] = new_app_seq[7]
            p.participant.vars['_updated_seq_apps'] = seq_to_dict(new_app_seq)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    username = models.StringField(blank=True)
    password = models.StringField(blank=True)
    check_password = models.IntegerField(blank=True)
    apps_show1 = models.StringField()
    apps_show2 = models.StringField()
    apps_show3 = models.StringField()
    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
