import pygame
from pathlib import Path

pygame.mixer.init()

class SoundEffects:
    """Plays sound effects"""
    SFX_FOLDER_DEFAULT = Path('./sounds')
    def __init__(self, **kwargs):
        self._sfx_folder = kwargs.get('sfx_folder', self.__class__.SFX_FOLDER_DEFAULT)
        self.bullet_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'bullet_fire.wav'))
        self.alien_hit_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'alien_hit.wav'))
        self.button_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'play_button.wav'))
        self.alien_edge_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'Alien_Edge.wav'))
        self.ship_hit_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'ship_hit.wav'))
        self.game_over_sound = pygame.mixer.Sound(Path(self._sfx_folder / 'game_over.wav'))
