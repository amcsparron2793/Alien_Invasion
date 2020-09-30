import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/bullet_fire.wav')
alien_sound = pygame.mixer.Sound('sounds/alien_hit.wav')
button_sound = pygame.mixer.Sound('sounds/play_button.wav')
alien_edge_sound = pygame.mixer.Sound('sounds/Alien_Edge.wav')
ship_hit_sound = pygame.mixer.Sound('sounds/ship_hit.wav')
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')