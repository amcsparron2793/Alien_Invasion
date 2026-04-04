class Settings:
    """ A class to store all the settings for Alien Invasion. """
    WHITE = (230, 230, 230)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    DEFAULT_SCREEN_WIDTH = 1200
    DEFAULT_SCREEN_HEIGHT = 800

    def __init__(self, **kwargs):
        """ Initialize the games static settings. """
        self._dark_mode = kwargs.get('dark_mode', False)

        # Screen Settings
        self.screen_width = kwargs.get('screen_width', self.__class__.DEFAULT_SCREEN_WIDTH)
        self.screen_height = kwargs.get('screen_height', self.__class__.DEFAULT_SCREEN_HEIGHT)
        self.bg_color = self.__class__.WHITE
        self.score_text_color = self.__class__.BLACK

        if self._dark_mode:
            self.bg_color = self.__class__.BLACK
            self.score_text_color = self.__class__.WHITE

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        # Dark grey bullets with a width of 3pix and a height of 15pix that moves slightly slower than the ship

        self.bullet_width = 3  # TODO: setting this to 300 is a good idea for a power-up
        self.bullet_height = 15
        self.bullet_color = self.__class__.BLACK
        if self._dark_mode:
            self.bullet_color = self.__class__.RED
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 5

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.25

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase Speed Settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)