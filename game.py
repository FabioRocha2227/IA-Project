import pygame
import time
import copy
from drawing import draw, draw_movement, draw_menu_initial, draw_menu_player, draw_menu_levels, draw_solution
from operators import move_right, move_up, move_down, move_left
from objective_test import objective_test
from utils_player import *
from data import timer_event, levels, players
from algorithm_BFS import breadth_first_search
from algorithm_IDFS import iterative_deepening_search
from algorithm_greedy import greedy_best_first_search
from algorithm_A_star import a_star
from utils_algorithms import print_solution


def menu():
    playing = True
    sub_menu = 0
    menu_initial_option = 0
    menu_player = 0
    menu_level = 0

    while playing == True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close the game's window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if sub_menu == 0:
                        if menu_initial_option != 0:
                            menu_initial_option -= 1
                    elif sub_menu == 1:
                        if menu_player > 1:
                            menu_player -= 2
                    elif sub_menu == 2:
                        if menu_level > 4 and menu_level != 10:
                            menu_level -= 5
                        if menu_level == 10:
                            menu_level = 7
                if event.key == pygame.K_DOWN:
                    if sub_menu == 0:
                        if menu_initial_option != 2:
                            menu_initial_option += 1
                    elif sub_menu == 1:
                        if menu_player < 4:
                            menu_player += 2
                    elif sub_menu == 2:
                        if menu_level < 5:
                            menu_level += 5
                        else:
                            menu_level = 10
                if event.key == pygame.K_LEFT:
                    if sub_menu == 1:
                        if menu_player % 2 != 0:
                            menu_player -= 1                        
                    elif sub_menu == 2:
                        if menu_level != 0 and menu_level != 5 and menu_level != 10:
                            menu_level -= 1
                if event.key == pygame.K_RIGHT:
                    if sub_menu == 1:
                        if menu_player % 2 == 0:
                            menu_player += 1
                    elif sub_menu == 2:
                        if menu_level != 4 and menu_level != 9 and menu_level != 10:
                            menu_level += 1
                if event.key == pygame.K_SPACE:
                    if sub_menu == 0:
                        if menu_initial_option == 2:
                            playing = False
                        else:
                            sub_menu = 1
                    elif sub_menu == 1:
                        if menu_player == 5:
                            sub_menu = 0
                            menu_initial_option = 0
                            menu_player = 0
                        else:
                            sub_menu = 2
                    elif sub_menu == 2:
                        if menu_level == 10:
                            sub_menu = 1
                            menu_level = 0
                        else:
                            level = copy.copy(levels[menu_level])
                            level.atoms_list = copy.deepcopy(levels[menu_level].atoms_list)
                            level.set_player(menu_player)
                            play(level)                     
                                 
        if sub_menu == 0:
            draw_menu_initial(menu_initial_option)
        elif sub_menu == 1:
            draw_menu_player(menu_player, players)
        else:
            draw_menu_levels(menu_level)
      
        
    

def play(level):
    playing = True

    while playing == True:
        # Human player
        if level.player == 0:
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
                            new_state = move_up(level.matrix, level.selected_atom, level.atoms_list)
                            draw_movement(level, new_state)
                        if event.key == pygame.K_DOWN:
                            new_state = move_down(level.matrix, level.selected_atom, level.atoms_list)
                            draw_movement(level, new_state)
                        if event.key == pygame.K_LEFT:
                            new_state = move_left(level.matrix, level.selected_atom, level.atoms_list)  
                            draw_movement(level, new_state)
                        if event.key == pygame.K_RIGHT: 
                            new_state = move_right(level.matrix, level.selected_atom, level.atoms_list)
                            draw_movement(level, new_state)
                        
                        # Check winning state after movement
                        if objective_test(level.matrix, level.atoms_list, level.molecule):
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
        # Algorithms  -  1.GREEDY   2.BFS   3.A-STAR   4.IDFS
        else:
            if level.player == 1:
                draw(level)
                goal = greedy_best_first_search(level)
                solution = print_solution(goal)
                draw_solution(level, solution)
                time.sleep(1.5)
                playing = False
            elif level.player == 2:
                draw(level)
                goal = breadth_first_search(level)
                solution = print_solution(goal)
                draw_solution(level, solution)
                time.sleep(1.5)
                playing = False
            elif level.player == 3:
                draw(level)
                goal = a_star(level)
                solution = print_solution(goal)
                draw_solution(level, solution)
                time.sleep(1.5)
                playing = False
            elif level.player == 4:
                draw(level)
                goal = iterative_deepening_search(level, 10)
                solution = print_solution(goal)
                draw_solution(level, solution)
                time.sleep(1.5)
                playing = False
