import pygame
import numpy as np
from globals import SQUARE_SIZE, RIGTH_OFFSET, DOWN_OFFSET, screen, clock, font, font_level_timeout, game_text_score, game_text_level, TEXT_COLOR, TEXT_ALERT_COLOR
from data_levels import *


def draw_player_position(level):
    selected_atom_index = np.where(level.state == level.selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]
    color = "red"
    if level.is_atom_picked == True:
        color = "yellow"
    pygame.draw.rect(screen, color, pygame.Rect(selected_atom_x * SQUARE_SIZE + RIGTH_OFFSET, selected_atom_y * SQUARE_SIZE + DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 3)



def draw_text():
    for i in range(0, 2):
        # Info about the player and the scores
        text = font.render(game_text_score[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, (i * 50 + 20)))

        # Info about the level and its timeout
        text = font.render(game_text_level[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, ((i + 1) * 50 + 100)))



def draw_scores():
    level_score, highscore = 0, 0
    text = font.render(str(level_score), True, TEXT_COLOR, None)
    screen.blit(text, (50, 35))
    text = font.render(str(highscore), True, TEXT_COLOR, None)
    screen.blit(text, (50, 85))



def draw_timeout(level_timeout):
    minutes = level_timeout // 60
    seconds = level_timeout - minutes * 60
    timeout = str(minutes) + ":"
    if seconds == 0:
        timeout += "00"
    elif seconds > 0 and seconds < 10:
        timeout += "0" + str(seconds)
    else:
        timeout += str(seconds)

    color = TEXT_COLOR
    if level_timeout <= 10:
        color = TEXT_ALERT_COLOR

    text = font_level_timeout.render(timeout, True, color, None)
    screen.blit(text, (50, 230))



def refresh():
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(15)
    


def draw(level, movement=False):  
    screen.fill(level.background_window)

    # Draw state
    for i in range(0, len(level.state[0])):
        for j in range(0, len(level.state)):
            if level.state[j][i] == -2:
                screen.blit(wall_extern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
                #pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level.state[j][i] == -1:
                screen.blit(wall_intern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
            elif level.state[j][i] == 0:
                pygame.draw.rect(screen, level.background_state, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level.state[j][i] > 0:
                pygame.draw.rect(screen, level.background_state, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
                if level.state[j][i] == level.selected_atom and not movement:
                    draw_player_position(level)
                #if not movement:  
                screen.blit(sprites_level_1[level.state[j][i]], (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))

    draw_text()
    draw_scores()
    draw_timeout(level.timeout)

    refresh()



def draw_movement(level, new_state):
    atom_index_old_state = np.where(level.state == level.selected_atom)
    old_state_atom_x, old_state_atom_y = atom_index_old_state[1][0], atom_index_old_state[0][0]
    atom_index_new_state = np.where(new_state == level.selected_atom)
    new_state_atom_x, new_state_atom_y = atom_index_new_state[1][0], atom_index_new_state[0][0]

    # Vertical direction
    while new_state_atom_y != old_state_atom_y:
        level.state[old_state_atom_y][old_state_atom_x] = 0

        if old_state_atom_y > new_state_atom_y:
            old_state_atom_y -= 1
        else:
            old_state_atom_y += 1

        level.state[old_state_atom_y][old_state_atom_x] = level.selected_atom

        draw(level, movement=True)
     
    # Horizontal direction
    while new_state_atom_x != old_state_atom_x:
        level.state[old_state_atom_y][old_state_atom_x] = 0

        if old_state_atom_x > new_state_atom_x:
            old_state_atom_x -= 1
        else:
            old_state_atom_x += 1

        level.state[old_state_atom_y][old_state_atom_x] = level.selected_atom

        draw(level, movement=True)
