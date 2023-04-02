import pygame
import numpy as np
from globals import SQUARE_SIZE, MOLECULE_SQUARE_SIZE
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
                    [-2, 0,-1, 0, 0,-1, 0,-1,-1, 0,-2],
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
molecule_atom_H_rigth = pygame.transform.scale(atom_H_rigth, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_O_left_rigth = pygame.image.load("sprites/O_left_right.png")
atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_left = pygame.image.load("sprites/H_left.png")
atom_H_left = pygame.transform.scale(atom_H_left, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_left = pygame.transform.scale(atom_H_left, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

sprites_level_1 = [atom_H_rigth, atom_O_left_rigth, atom_H_left]
molecule_sprites_level_1 = [molecule_atom_H_rigth, molecule_atom_O_left_rigth, molecule_atom_H_left]

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

#Level 4

#11x13
matrix_level_4 =   [[-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3],
                    [-2, 0,-1, 0, 0, 0,-2,-3,-3,-3,-3],
                    [-2, 0,-1, 0,-1, 0,-2,-3,-3,-3,-3],
                    [-2, 0,-1, 0, 0, 0,-2,-3,-3,-3,-3],
                    [-2, 0,-1, 0, 0, 0,-2,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-2,-2,-2,-2,-2,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0,-1,-1, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0, 0, 0, 0,-1,-1,-1,-2],
                    [-2,-1, 0, 0,-1, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0,-1, 0,-1, 0, 0, 0,-2],
                    [-2, 0, 0, 0,-1, 0, 0, 0,-2,-2,-2],
                    [-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3]]

molecule_level_4 = [[ 0,-1,-1, 1],
                    [-1, 1, 2,-1],
                    [ 3,-1,-1, 4]]

atoms_list_level_4 = [[5,9], [7,7], [5,7], [2,7], [3,2], [3,11]]

timeout_level_4 = 360

atom_H_leftdown = pygame.transform.rotate(atom_H_left, 45)
atom_H_leftup = pygame.transform.rotate(atom_H_up, 45)
atom_H_rightdown = pygame.transform.rotate(atom_H_down, 45)
atom_H_rightup = pygame.transform.rotate(atom_H_rigth, 45)

sprites_level_4 = [atom_H_rightdown, atom_H_leftdown, atom_O_left_rigth, atom_O_left_rigth, atom_H_rightup, atom_H_leftup]

#Level 5

matrix_level_5 =   [[-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-3,-3,-3,-3],
                    [-3,-3,-2,-2,-2,-2,-2, 0, 0,-2,-3,-3,-3,-3],
                    [-3,-3,-2, 0, 0, 0, 0, 0, 0,-2,-3,-3,-3,-3],
                    [-3,-3,-2, 0, 0, 0,-1,-1,-1,-2,-2,-2,-2,-2],
                    [-3,-3,-2, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2],
                    [-3,-3,-2,-1,-1,-1, 0, 0,-1,-1, 0, 0, 0,-2],
                    [-2,-2,-2, 0, 0,-1, 0, 0, 0,-1, 0, 0, 0,-2],
                    [-2, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0,-1, 0, 0,-1, 0,-1,-1,-1,-1,-1,-1,-2],
                    [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-2, 0, 0, 0,-1, 0, 0, 0, 0,-1,-1, 0, 0,-2],
                    [-2, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]]

molecule_level_5 = [[-1, 0, 1,-1, 2],
                    [ 3, 4, 5, 6,-1],
                    [-1, 7,-1,-1, 8]]

atoms_list_level_5 = [[5,3], [10,7], [8,2], [3,6], [8,6], [3,4], [11,5], [9, 11], [1,11]]

sprites_level_5 = [atom_H_down, atom_H_down, atom_H_leftdown, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_up, atom_H_leftup]

#Level 6

matrix_level_6 = [[-2,-2,-2,-2,-2,-2],
                  [-2, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0, 0,-2],
                  [-2,-2,-2,-2,-2,-2]]

molecule_level_6 = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7,-1]]

atoms_list_level_6 = [[1,3], [4,1], [3,4], [2,1], [4,3], [1,4], [2,2], [3,2]]

sprites_level_6 = [atom_H_rightdown, atom_H_down, atom_H_leftdown, atom_H_rigth, atom_O_left_rigth, atom_H_left, atom_H_rightup, atom_H_up]

#Level 7

matrix_level_7 = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3],
                  [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0,-2,-3,-3],
                  [-2, 0,-1,-1, 0, 0,-1, 0, 0, 0,-2,-3,-3],
                  [-2, 0, 0, 0, 0, 0, 0,-1, 0, 0,-2,-3,-3],
                  [-2, 0, 0, 0,-1, 0, 0,-1, 0, 0,-2,-3,-3],
                  [-2, 0,-1, 0,-1, 0, 0,-1, 0, 0,-2,-3,-3],
                  [-2, 0, 0, 0, 0, 0, 0, 0, 0,-1,-2,-2,-2],
                  [-2,-2,-1,-1,-1, 0, 0,-1, 0, 0, 0, 0,-2],
                  [-3,-2, 0, 0, 0, 0, 0,-1, 0,-1, 0, 0,-2],
                  [-2,-2, 0,-1,-1, 0, 0, 0, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0, 0, 0, 0, 0,-2,-2,-2,-2,-2],
                  [-2, 0, 0, 0, 0, 0,-1, 0,-2,-3,-3,-3,-3],
                  [-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3]]

molecule_level_7 = [[-1, 0, 1,-1,-1],
                    [ 2, 3, 4, 5, 6],
                    [-1, 7, 8,-1,-1]]

atoms_list_level_7 = [[3,1], [9,9], [2,9], [6,3], [8,5], [5,8], [3,5], [6,10], [4, 11]]

sprites_level_7 = [atom_H_down, atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_left, atom_H_up, atom_H_up]

#Level 8

matrix_level_8 = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3],
                  [-2, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2,-3],
                  [-2, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2,-3],
                  [-2, 0, 0,-1, 0, 0, 0, 0, 0, 0,-2,-3],
                  [-2, 0, 0,-1, 0,-1,-1,-1,-1, 0,-2,-2],
                  [-2, 0, 0,-1, 0,-1, 0, 0,-1, 0, 0,-2],
                  [-2, 0,-1,-1, 0, 0, 0, 0,-1, 0, 0,-2],
                  [-2, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-2],
                  [-2, 0, 0,-1, 0, 0, 0,-1,-1, 0, 0,-2],
                  [-2, 0, 0,-1,-1, 0, 0, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0,-1, 0, 0, 0, 0,-1,-1,-2],
                  [-2, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0,-2],
                  [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]]

molecule_level_8 = [[-1, 0, 1, 2,-1],
                    [ 3, 4, 5, 6, 7],
                    [-1, 8, 9,10,-1],
                    [-1,-1,11,-1,-1]]

atoms_list_level_8 = [[8,1], [2,4], [9,7], [3,10], [2,8], [7,10], [9,5], [9,9], [4,4], [6,3], [7,5], [7,9]]

atom_O_up_down = pygame.transform.rotate(atom_O_left_rigth, 90)

sprites_level_8 = [atom_H_down, atom_H_down, atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_left, atom_H_up, atom_O_up_down, atom_H_up, atom_H_up]

#Level 9

matrix_level_9 = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                  [-2, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                  [-2, 0, 0,-1,-1,-1, 0,-1, 0,-2],
                  [-2, 0, 0, 0, 0, 0, 0,-1, 0,-2],
                  [-2, 0,-1,-1, 0, 0, 0, 0, 0,-2],
                  [-2, 0, 0, 0, 0, 0, 0,-1, 0,-2],
                  [-2, 0,-1,-1,-1,-1, 0,-1, 0,-2],
                  [-2, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                  [-2, 0,-1, 0, 0,-2,-2,-2,-2,-2],
                  [-2, 0,-1, 0, 0,-2,-3,-3,-3,-3],
                  [-2,-2,-2,-2,-2,-2,-3,-3,-3,-3]]

molecule_level_9 = [[-1, 0, 1,-1],
                    [ 2, 3, 4, 5],
                    [-1, 6,-1,-1]]

atoms_list_level_9 = [[8,5], [6,3], [2,5], [6,4], [4,7], [7,1], [5,5]]

sprites_level_9 = [atom_H_down, atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_up]

#Level 10

matrix_level_10 = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,],
                   [-2, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0,-2,],
                   [-2, 0, 0,-1, 0, 0, 0,-1, 0, 0,-1,-1,-2,],
                   [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-2,],
                   [-2,-2,-2,-1,-1,-1,-1,-1,-1, 0, 0, 0,-2,],
                   [-3,-3,-2, 0, 0, 0, 0, 0,-1, 0, 0, 0,-2,],
                   [-3,-3,-2, 0, 0,-1, 0, 0, 0, 0, 0, 0,-2,],
                   [-2,-2,-2, 0, 0, 0, 0, 0, 0, 0,-1, 0,-2,],
                   [-2, 0, 0, 0,-1, 0, 0, 0, 0, 0,-1, 0,-2,],
                   [-2, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0,-2,],
                   [-2, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0,-2,],
                   [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,]]

molecule_level_10 = [[-1, 0,-1, 1,-1],
                     [ 2, 3, 4, 5, 6],
                     [-1, 7, 8, 9,-1]]

atoms_list_level_10 = [[7,3], [9,5], [4,9], [6,7], [8,7], [10,5], [9,2], [3,1], [9,8], [3,3]]

sprites_level_10 = [atom_H_down, atom_H_down, atom_H_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_O_left_rigth, atom_H_left, atom_H_up, atom_O_up_down, atom_H_up]


# Levels list
level_1 = Level(matrix_level_1, molecule_level_1, atoms_list_level_1, timeout_level_1, sprites_level_1, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_2 = Level(matrix_level_2, molecule_level_2, atoms_list_level_2, timeout_level_1, sprites_level_2, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_3 = Level(matrix_level_3, molecule_level_3, atoms_list_level_3, timeout_level_1, sprites_level_3, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_4 = Level(matrix_level_4, molecule_level_4, atoms_list_level_4, timeout_level_4, sprites_level_4, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_5 = Level(matrix_level_5, molecule_level_5, atoms_list_level_5, timeout_level_4, sprites_level_5, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_6 = Level(matrix_level_6, molecule_level_6, atoms_list_level_6, timeout_level_1, sprites_level_6, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_7 = Level(matrix_level_7, molecule_level_7, atoms_list_level_7, timeout_level_4, sprites_level_7, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_8 = Level(matrix_level_8, molecule_level_8, atoms_list_level_8, timeout_level_4, sprites_level_8, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_9 = Level(matrix_level_9, molecule_level_9, atoms_list_level_9, timeout_level_4, sprites_level_9, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)
level_10 = Level(matrix_level_10, molecule_level_10, atoms_list_level_10, timeout_level_4, sprites_level_10, molecule_sprites_level_1, background_window_level_1, background_matrix_level_1)

levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10]
