from pathlib import Path
PROJECT_BASE_DIR = Path('./AlienInvasion')

from AlienInvasion import Backend, Sprites
from AlienInvasion.alien_invasion import AlienInvasion

__all__ = ['PROJECT_BASE_DIR', 'Sprites', 'Backend', 'AlienInvasion']