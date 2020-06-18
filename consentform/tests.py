from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.InformedConsent, {'consent': random.choice([True, False])})
        if not self.player.consent:
            yield (pages.InformedConsent2, {'consent2': True})
