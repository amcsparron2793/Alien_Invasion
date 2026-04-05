from pathlib import Path


class GameStats:
    """ Track statistics for Alien Invasion. """
    DEFAULT_HIGHSCORE_PATH = './Current_HighScore.txt'
    DEFAULT_LEVEL = 3

    def __init__(self, ai_game):
        """ Initialize statistics. """
        self.game = ai_game
        self.settings = self.game.settings
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = self.__class__.DEFAULT_LEVEL
        self.highscore = 0

        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        self.init_highscore()

    def init_highscore(self):
        # Highscore never needs to be reset
        try:
            with open(self.__class__.DEFAULT_HIGHSCORE_PATH, 'r') as f:
                self.highscore = int(f.read())
        except FileNotFoundError:
            Path(self.__class__.DEFAULT_HIGHSCORE_PATH).touch()
            self.highscore = 0
        except ValueError:
            self.highscore = 0

    def write_highscore(self):
        if Path(self.__class__.DEFAULT_HIGHSCORE_PATH).is_file():
            with open(self.__class__.DEFAULT_HIGHSCORE_PATH, 'a') as file:
                file.truncate(0)
                file.write(str(self.highscore))
        elif not Path(self.__class__.DEFAULT_HIGHSCORE_PATH).is_file():
            with open(self.__class__.DEFAULT_HIGHSCORE_PATH, 'w') as file:
                file.write(str(self.highscore))


    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = self.__class__.DEFAULT_LEVEL
