from os import environ
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_lazy

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


SESSION_CONFIGS = [
    dict(
        name='Relative_income',
        display_name='Relative income',
        num_demo_participants=200,
        app_sequence=['consentform', 'background_que', 'beliefs', 'preferred_info', 'stimuli', 'job_salary',
                      'just_world', 'political_pref', 'social_pref', 'incentivized_tasks', 'summary'],
    ),
    dict(
        name='Relative_income_alt',
        display_name='Relative income alt',
        num_demo_participants=200,
        app_sequence=['consentform', 'background_que', 'beliefs', 'preferred_info', 'stimuli', 'job_salary',
                      'just_world', 'political_pref', 'social_pref', 'incentivized_tasks', 'summary'],
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'fi'
LANGUAGE_SESSION_KEY = '_language'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='2',
        display_name='stat2',
        participant_label_file='_rooms/stat_users_simulated_main.txt',
    ),
    dict(
        name='3',
        display_name='stat3',
        participant_label_file='_rooms/stat_users_simulated_noincentive_main.txt',
    ),
    dict(
        name='live_demo',
        display_name='Room for live demo (no participant labels)',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '_e0g+l9t2hb+ujn5(mev6r0bkw@_p2l1xx*6i72gs0950^7+u%'

INSTALLED_APPS = ['otree']
MIDDLEWARE_CLASSES = ['django.middleware.locale.LocaleMiddleware', ]
