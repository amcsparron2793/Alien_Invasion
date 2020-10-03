from alien_invasion import AlienInvasion


class AIPlayer:

    def __init__(self, ai_game):
        """Automatic player for alien invasion."""

        # need a reference to the game object.
        self.ai_game = ai_game

    def run_game(self):
        """Replaces the original run game(), so that we can interject our own controls."""

        # start out in an active state
        self.ai_game.stats.game_active = True

        # start the main loop for the game
