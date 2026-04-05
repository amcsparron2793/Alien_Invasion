import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """ A class to report scoring information. """
    SCORE_RECT_RIGHT_TOP_OFFSET = 20
    LEVEL_RECT_BOTTOM_OFFSET = 10
    SHIP_COUNT_X_RECT_OFFSET = 10
    SHIP_COUNT_Y_RECT_OFFSET = 10

    def __init__(self, ai_game):
        """ Init scorekeeping attributes. """
        self.level_rect = None
        self.score_rect = None
        self.highscore_rect = None
        self.ships = None
        self.highscore_image = None
        self.score_image = None
        self.level_image = None

        self.game = ai_game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = self.game.settings
        self.stats = self.game.stats

        # font settings for scoring information
        self.text_color = self.settings.score_text_color
        self.font = pygame.font.SysFont(None, 48)
        # Prep the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """ Show how many ships you have left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = self.__class__.SHIP_COUNT_X_RECT_OFFSET + ship_number * ship.rect.width
            ship.rect.y = self.__class__.SHIP_COUNT_Y_RECT_OFFSET  # one row of ships - places row below score
            self.ships.add(ship)

    def prep_high_score(self):
        """ Turn the high score into a rendered image. """

        highscore = round(self.stats.highscore, -1)
        highscore_str = f"{highscore:,}"
        self.highscore_image = self.font.render(highscore_str, True,
                                                self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def prep_score(self):
        """ Turn the score value into a rendered image. """
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - self.__class__.SCORE_RECT_RIGHT_TOP_OFFSET
        self.score_rect.top = self.__class__.SCORE_RECT_RIGHT_TOP_OFFSET

    def show_score(self):
        """ Draw scores, level and ships to the screen. """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """ Check to see if there's a new high score. """
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image. """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + self.__class__.LEVEL_RECT_BOTTOM_OFFSET
