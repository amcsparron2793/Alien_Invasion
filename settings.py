class Settings:
    """ A class to store all the settings for Alien Invasion. """
    WHITE = (230, 230, 230)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, **kwargs):
        """ Initialize the games static settings. """
        self._dark_mode = None
        try:
            if kwargs['dark_mode']:
                self._dark_mode = kwargs['dark_mode']
        except KeyError:
            pass

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self.WHITE
        self.score_text_color = self.BLACK

        if self._dark_mode:
            self.bg_color = self.BLACK
            self.score_text_color = self.WHITE

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        # Dark grey bullets with a width of 3pix and a height of 15pix that moves slightly slower than the ship

        self.bullet_width = 3  # TODO: setting this to 300 is a good idea for a powerup
        self.bullet_height = 15
        self.bullet_color = self.BLACK
        if self._dark_mode:
            self.bullet_color = self.RED
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