class Settings:
    """ A class to store all the settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the games static settings. """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        # Bullet settings
        # Dark grey bullets with a width of 3pix and a height of 15pix that moves slightly slower than the ship
        self.bullet_speed = 1.5
        self.bullet_width = 3  # TODO: setting this to 300 is a good idea for a powerup
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 0.75
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.75

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