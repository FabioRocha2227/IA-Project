import pygame
from data_levels import levels
from game import play



level = levels[0]

#while menu() > 0:
play(level)

pygame.quit()