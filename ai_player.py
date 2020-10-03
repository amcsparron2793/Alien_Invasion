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
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to quit.
            self.ai_game._check_events()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()
                self.ai_game._fire_bullet()

            self.ai_game._update_screen()


if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()
