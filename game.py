import pygame
import time
from drawing import draw, draw_movement
from operators import move_right, move_up, move_down, move_left
from objective_test import objective_test
from utils_player import *
from globals import timer_event


#def menu():
    

def play(level):
    playing = True

    while playing == True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close the game's window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if level.is_atom_picked == False:
                        level.is_atom_picked = True
                    else:
                        level.is_atom_picked = False
                # Commands to choose atom
                if level.is_atom_picked == False:
                    if event.key == pygame.K_UP:
                        select_atom_up(level)
                    if event.key == pygame.K_DOWN:
                        select_atom_down(level)
                    if event.key == pygame.K_LEFT:
                        select_atom_left(level)
                    if event.key == pygame.K_RIGHT:
                        select_atom_right(level)
                # Commands to move atom
                else:
                    if event.key == pygame.K_UP:
                        new_state = move_up(level.state, level.selected_atom)
                        draw_movement(level, new_state)
                    if event.key == pygame.K_DOWN:
                        new_state = move_down(level.state, level.selected_atom)
                        draw_movement(level, new_state)
                    if event.key == pygame.K_LEFT:
                        new_state = move_left(level.state, level.selected_atom)  
                        draw_movement(level, new_state)
                    if event.key == pygame.K_RIGHT: 
                        new_state = move_right(level.state, level.selected_atom)
                        draw_movement(level, new_state)
                    
                    # Check winning state after movement
                    if objective_test(level.state, level.molecule):
                        playing = False
                        print("WIN")
                        time.sleep(1.5)
            elif event.type == timer_event:
                level.timeout -= 1
                if level.timeout == 0:
                    print("GAMEOVER")
                    time.sleep(1.5)
                    playing = False

        draw(level)
