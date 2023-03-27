import pygame
import numpy as np
from globals import SQUARE_SIZE
from level import Level

# Global sprites

wall_extern = pygame.image.load("sprites/wall_extern.png")
wall_extern = pygame.transform.scale(wall_extern, (SQUARE_SIZE, SQUARE_SIZE))

wall_intern = pygame.image.load("sprites/wall_intern.png")
wall_intern = pygame.transform.scale(wall_intern, (SQUARE_SIZE, SQUARE_SIZE))



# Levels

# Level 1

matrix_level_1 =   [[-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-2,-2,-2,-2,-2,-3],
                    [-2, 0, 0,-1, 0, 0, 0, 0, 0,-2,-3],
                    [-2, 0,-1, 0, 0, 0, 0, 0, 0,-2,-2],
                    [-2, 0, -1, 0, 0,-1, 0,-1,-1, 0,-2],
                    [-2, 0, 0, 0, 0,-1, 0,-1, 0, 0,-2],
                    [-2,-2,-1, 0,-1, 0, 0,-1, 0, 0,-2],
                    [-3,-2, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]]

molecule_level_1 = [[0,1,2]]
atoms_list_level_1 = [[3,7], [8,6], [3,2]]
#molecule_level_1 = [[0,1,2,-1],[-1,-1,3,4]]
#atoms_list_level_1 = [[1,2],[2,2],[3,2],[3,3],[4,3]]

timeout_level_1 = 120

background_window_level_1 = "#2F2D29"#F1DDBF"
background_matrix_level_1 = "#FFB562"

atom_H_rigth = pygame.image.load("sprites/H_right.png")
atom_H_rigth = pygame.transform.scale(atom_H_rigth, (SQUARE_SIZE, SQUARE_SIZE))

atom_O_left_rigth = pygame.image.load("sprites/O_left_right.png")
atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (SQUARE_SIZE, SQUARE_SIZE))

atom_H_left = pygame.image.load("sprites/H_left.png")
atom_H_left = pygame.transform.scale(atom_H_left, (SQUARE_SIZE, SQUARE_SIZE))

sprites_level_1 = [atom_H_rigth, atom_O_left_rigth, atom_H_left]

# Level 2

matrix_level_2 =   [[-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                    [-2, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0, 0,-2],
                    [-2, 0, 0,-1, 0, 0,-1,-1,-1,-1,-1, 0, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0,-2],
                    [-2, 0,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0,-1, 0, 0,-2,-2,-2,-2,-2,-2,-2],
                    [-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3]]

molecule_level_2 = [[-1, 0,-1],
                    [ 1, 2, 3],
                    [-1, 4,-1]]
atoms_list_level_2 = [[9,4], [2,5], [5,4], [8,8], [3,9]]

atom_H_up = pygame.transform.rotate(atom_H_rigth, 90)
atom_H_down = pygame.transform.rotate(atom_H_left, 90)

sprites_level_2 = [atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_H_left, atom_H_up]



#Level 3

matrix_level_3 =   [[-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3],
                    [-2, 0, 0, 0,-1, 0, 0, 0,-1, 0,-2,-2,-2],
                    [-2, 0,-1, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2],
                    [-2, 0, 0,-1,-1,-1, 0, 0,-1, 0,-1, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0,-2],
                    [-2,-2,-2,-2,-2,-2, 0, 0, 0, 0,-1, 0,-2],
                    [-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2]]

molecule_level_3 = [[-1, 0,-1,-1],
                    [ 1, 2, 3, 4],
                    [-1, 5,-1,-1]]
atoms_list_level_3 = [[2,3], [2,8], [9,7], [6,8], [8,10], [5,10]]

sprites_level_3 = [atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_left, atom_H_up]

# Levels list
level_1 = Level(matrix_level_1, molecule_level_1, atoms_list_level_1, timeout_level_1, sprites_level_1, background_window_level_1, background_matrix_level_1)
level_2 = Level(matrix_level_2, molecule_level_2, atoms_list_level_2, timeout_level_1, sprites_level_2, background_window_level_1, background_matrix_level_1)
level_3 = Level(matrix_level_3, molecule_level_3, atoms_list_level_3, timeout_level_1, sprites_level_3, background_window_level_1, background_matrix_level_1)

levels = [level_1, level_2, level_3]