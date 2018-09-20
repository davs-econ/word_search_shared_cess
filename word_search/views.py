from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class WordPuzzle(Page):
    timeout_seconds = Constants.word_puzzle_seconds + 1


class WordsFound(Page):
    form_model = models.Player
    form_fields = ['words_found']


class RegularWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_word_search_payoff()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    RegularWaitPage,
    WordPuzzle,
    WordsFound,
    ResultsWaitPage
]
