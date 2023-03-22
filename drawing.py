import pygame
import numpy as np
from globals import SQUARE_SIZE, RIGTH_OFFSET, DOWN_OFFSET, screen, clock
from data_levels import *


def draw_player_position(level_state, selected_atom, picked_atom):
    selected_atom_index = np.where(level_state == selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]
    color = "red"
    if picked_atom == True:
        color = "yellow"
    pygame.draw.rect(screen, color, pygame.Rect(selected_atom_x * SQUARE_SIZE + RIGTH_OFFSET, selected_atom_y * SQUARE_SIZE + DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 3)



def refresh():
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(15)
    


def draw(level_state, selected_atom, picked_atom, movement=False):  
 # fill the screen with a color to wipe away anything from last frame
    #screen.fill("#D8D8D8")
    screen.fill(background_level_1)

    for i in range(0, len(level_state[0])):
        for j in range(0, len(level_state)):
            if level_state[j][i] == -2:
                screen.blit(wall_extern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
                #pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level_state[j][i] == -1:
                screen.blit(wall_intern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
            elif level_state[j][i] == 0:
                pygame.draw.rect(screen, background_secondary_level_1, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level_state[j][i] > 0:
                pygame.draw.rect(screen, background_secondary_level_1, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
                if level_state[j][i] == selected_atom and not movement:
                    draw_player_position(level_state, selected_atom, picked_atom)
                #if not movement:  
                screen.blit(sprites_level_1[level_state[j][i]], (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))

    refresh()