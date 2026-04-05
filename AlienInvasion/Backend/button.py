import pygame.font

class Button:
    """ A button class to handle the play button. """
    DEFAULT_BUTTON_WIDTH = 200
    DEFAULT_BUTTON_HEIGHT = 50

    def __init__(self, ai_game, msg, **kwargs):
        """ Init button attributes. """
        self.game = ai_game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = (kwargs.get('width', self.__class__.DEFAULT_BUTTON_WIDTH),
                                   kwargs.get('height', self.__class__.DEFAULT_BUTTON_HEIGHT))
        self.button_color = kwargs.get('button_color', self.game.settings.__class__.GREEN)
        self.text_color = kwargs.get('text_color', self.game.settings.__class__.WHITE)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on the button. """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw the blank button and then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)