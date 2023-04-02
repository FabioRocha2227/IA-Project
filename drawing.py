import pygame
import numpy as np
from globals import SQUARE_SIZE, RIGTH_OFFSET, DOWN_OFFSET, screen, clock, font, font_molecule_name, font_level_timeout, game_text_score, game_text_level, TEXT_COLOR, TEXT_ALERT_COLOR
from data_levels import *
from data_levels import wall_extern, wall_intern


def draw_player_position(level):
    color = "red"
    if level.is_atom_picked == True:
        color = "yellow"
    pygame.draw.rect(screen, color, pygame.Rect(level.atoms_list[level.selected_atom][0] * SQUARE_SIZE + RIGTH_OFFSET, level.atoms_list[level.selected_atom][1] * SQUARE_SIZE + DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 3)



def draw_atoms(level, movement):
    for i in range(0, len(level.atoms_list)):
        if i == level.selected_atom and not movement:
            draw_player_position(level)
        screen.blit(level.sprites[i], (level.atoms_list[i][0] * SQUARE_SIZE+RIGTH_OFFSET, level.atoms_list[i][1] * SQUARE_SIZE+DOWN_OFFSET))



def draw_text():
    for i in range(0, 2):
        # Info about the player and the scores
        text = font.render(game_text_score[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, (i * 50 + 20)))

        # Info about the level and its timeout
        text = font.render(game_text_level[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, ((i + 1) * 70 + 80)))

    # Current level
    text = font_level_timeout.render("1", True, TEXT_COLOR, None)
    screen.blit(text, (50, 170))



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
    screen.blit(text, (50, 240))



def draw_molecule(level):
    pygame.draw.rect(screen, "#1B1B1B", pygame.Rect(50, 300, 125, 150))
    pygame.draw.rect(screen, "#131313", pygame.Rect(50, 300, 125, 150), 3)
    pygame.draw.rect(screen, "#363636", pygame.Rect(53, 303, 120, 25))
    text = font.render("- MOLECULE -", True, "#9D9D9D", None)
    screen.blit(text, (72, 310))
    text = font_molecule_name.render("WATER", True, "#787878", None)
    screen.blit(text, (95, 335))
    for i in range(0, len(level.molecule)):
        for j in range(0, len(level.molecule[0])):
            screen.blit(level.molecule_sprites[level.molecule[i][j]], (88 + j * MOLECULE_SQUARE_SIZE, 355 + i * MOLECULE_SQUARE_SIZE))



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
    for i in range(0, len(level.matrix[0])):
        for j in range(0, len(level.matrix)):
            if level.matrix[j][i] == -2:
                screen.blit(wall_extern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
                #pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level.matrix[j][i] == -1:
                screen.blit(wall_intern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
            elif level.matrix[j][i] >= 0:
                pygame.draw.rect(screen, level.background_matrix, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))

    draw_atoms(level, movement)
    draw_text()
    draw_scores()
    draw_timeout(level.timeout)
    draw_molecule(level)

    refresh()



def draw_movement(level, new_state):
    old_state_atom_x, old_state_atom_y = level.atoms_list[level.selected_atom][0], level.atoms_list[level.selected_atom][1]
    new_state_atom_x, new_state_atom_y = new_state[level.selected_atom][0], new_state[level.selected_atom][1]
    # Vertical direction
    while new_state_atom_y != old_state_atom_y:
        if old_state_atom_y > new_state_atom_y:
            old_state_atom_y -= 1
        else:
            old_state_atom_y += 1

        level.atoms_list[level.selected_atom][1] = old_state_atom_y

        draw(level, movement=True)
     
    # Horizontal direction
    while new_state_atom_x != old_state_atom_x:
        if old_state_atom_x > new_state_atom_x:
            old_state_atom_x -= 1
        else:
            old_state_atom_x += 1

        level.atoms_list[level.selected_atom][0] = old_state_atom_x

        draw(level, movement=True)
