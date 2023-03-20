import pygame
import levels
from drawing import draw
from movement import move_right, move_up, move_down, move_left
from winningstate import winning_state

# screen is imported - singleton
# clock is imported
running = True

# Level variables
level = levels.level1
atoms_list = levels.atoms_list_level1
molecule = levels.molecule_level1
selected_atom = 0
is_atom_picked = False


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
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
                if event.key == pygame.K_LEFT:
                    if selected_atom == 0:
                        selected_atom = len(atoms_list) - 1                 
                    else:
                        selected_atom = selected_atom - 1
                if event.key == pygame.K_RIGHT:
                    if selected_atom == len(atoms_list) - 1:
                        selected_atom = 0
                    else:
                        selected_atom = selected_atom + 1
            # Commands to move atom
            else:
                if event.key == pygame.K_UP:
                    move_up(level, atoms_list, selected_atom)  
                if event.key == pygame.K_DOWN:
                    move_down(level, atoms_list, selected_atom)  
                if event.key == pygame.K_LEFT: 
                    move_left(level, atoms_list, selected_atom)  
                if event.key == pygame.K_RIGHT: 
                     move_right(level, atoms_list, selected_atom)  
                

                print(level)
                # TODO: Check winning state after movement
                if winning_state(level, molecule, atoms_list):
                    running = False


    draw(level, atoms_list, selected_atom, is_atom_picked)

pygame.quit()