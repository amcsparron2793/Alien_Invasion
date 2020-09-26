from os.path import isfile


class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_game):
        """ Initialize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

        # start Alien Invasion in an active state
        self.game_active = False

        # high score never needs to be reset
        if isfile('./Current_HighScore.txt'):
            with open('./Current_HighScore.txt', 'r') as file:
                file.read = int(self.high_score)
            file.close()
        elif not isfile('./Current_HighScore.txt'):
            self.high_score = 0

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
