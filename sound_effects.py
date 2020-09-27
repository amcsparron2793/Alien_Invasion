import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/laser1.wav')
alien_sound = pygame.mixer.Sound('sounds/Explosion_02.wav')
button_sound = pygame.mixer.Sound('sounds/button.wav')
alien_edge_sound = pygame.mixer.Sound('sounds/Game_Over.wav')
ship_hit_sound = pygame.mixer.Sound('sounds/Grenade.wav')
game_over_sound = pygame.mixer.Sound('sounds/Game_Over.wav')