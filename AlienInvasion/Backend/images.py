import pygame
from pathlib import Path
from AlienInvasion import PROJECT_BASE_DIR

class Images:
    """A class to manage all images in the game"""
    IMAGES_FOLDER_DEFAULT = Path(PROJECT_BASE_DIR.parent, 'imgs')

    def __init__(self, **kwargs):
        self._images_folder = kwargs.get('images_folder', self.__class__.IMAGES_FOLDER_DEFAULT)
        self.alien_image = pygame.image.load(Path(self._images_folder / 'alien.bmp'))
        self.ship_image = pygame.image.load(Path(self._images_folder / 'ship.bmp'))