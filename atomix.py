import pygame
import numpy as np
import time
import data_levels
from drawing import draw, draw_movement
from operators import move_right, move_up, move_down, move_left
from objective_test import objective_test
from utils import *
from globals import timer_event

# screen is imported - singleton
# clock is imported
running = True

# Level variables
level_state = data_levels.level_1.copy()
molecule = data_levels.molecule_level_1
selected_atom = 1
is_atom_picked = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the game's window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_atom_picked == False:
                    is_atom_picked = True
                else:
                    is_atom_picked = False
            # Commands to choose atom
            if is_atom_picked == False:
                if event.key == pygame.K_UP:
                    selected_atom = select_atom_up(level_state, selected_atom)
                if event.key == pygame.K_DOWN:
                    selected_atom = select_atom_down(level_state, selected_atom)
                if event.key == pygame.K_LEFT:
                    selected_atom = select_atom_left(level_state, selected_atom)
                if event.key == pygame.K_RIGHT:
                    selected_atom = select_atom_right(level_state, selected_atom)
            # Commands to move atom
            else:
                if event.key == pygame.K_UP:
                    new_state = move_up(level_state, selected_atom)
                    draw_movement(level_state, new_state, selected_atom, data_levels.timeout_level_1)
                if event.key == pygame.K_DOWN:
                    new_state = move_down(level_state, selected_atom)
                    draw_movement(level_state, new_state, selected_atom, data_levels.timeout_level_1)
                if event.key == pygame.K_LEFT: 
                    new_state = move_left(level_state, selected_atom)  
                    draw_movement(level_state, new_state, selected_atom, data_levels.timeout_level_1)
                if event.key == pygame.K_RIGHT: 
                    new_state = move_right(level_state, selected_atom)
                    draw_movement(level_state, new_state, selected_atom, data_levels.timeout_level_1)  
                
                # Check winning state after movement
                if objective_test(level_state, molecule):
                    running = False
        elif event.type == timer_event:
            data_levels.timeout_level_1 -= 1
            if data_levels.timeout_level_1 == 0:
                print("GAMEOVER")
                time.sleep(1.5)
                running = False

    draw(level_state, selected_atom, is_atom_picked, data_levels.timeout_level_1)

pygame.quit()