from os.path import isfile
from os import system


class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_game):
        """ Initialize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

        # start Alien Invasion in an active state
        self.game_active = False

        # high score never needs to be reset
        # MY CODE BELOW
        """
        if isfile('./Current_HighScore.txt'):
            with open('./Current_HighScore.txt', 'r') as file:
                self.high_score = int(file.read())
        elif not isfile('./Current_HighScore.txt'):
            system('pause')"""
        self.high_score = 0

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
