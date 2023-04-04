import pygame
from level import Level
from atom import Atom

# Macros

SQUARE_SIZE = 32
MOLECULE_SQUARE_SIZE = 16

TEXT_COLOR = "white"
TEXT_ALERT_COLOR = "red"

# pygame setup

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Atomix (Group 86)')
clock = pygame.time.Clock()

# Timer
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , 1000)

# Fonts

font = pygame.font.SysFont(",", 18)
font_molecule_name = pygame.font.SysFont(",", 14)
font_48 = pygame.font.SysFont(",", 48)
font_menu_10 = pygame.font.Font("assets/fonts/Boeing.ttf", 10)
font_menu_14 = pygame.font.Font("assets/fonts/Boeing.ttf", 14)
font_menu_16 = pygame.font.Font("assets/fonts/Boeing.ttf", 16)
font_menu_22 = pygame.font.Font("assets/fonts/Boeing.ttf", 22)
font_menu_26 = pygame.font.Font("assets/fonts/Boeing.ttf", 26)
font_menu_30 = pygame.font.Font("assets/fonts/Boeing.ttf", 30)
font_menu_36 = pygame.font.Font("assets/fonts/Boeing.ttf", 36)
font_verdana_10 = pygame.font.SysFont("Verdana", 10)

# Sprites

atomix_logo = pygame.image.load("assets/sprites/Atomix_logo.png")
atomix_logo = pygame.transform.scale(atomix_logo, (256, 270))

wall_extern = pygame.image.load("assets/sprites/wall_extern.png")
wall_extern = pygame.transform.scale(wall_extern, (SQUARE_SIZE, SQUARE_SIZE))

wall_intern = pygame.image.load("assets/sprites/wall_intern.png")
wall_intern = pygame.transform.scale(wall_intern, (SQUARE_SIZE, SQUARE_SIZE))

# Hidrogen 

atom_H_rigth = pygame.image.load("assets/sprites/H_right.png")
atom_H_rigth = pygame.transform.scale(atom_H_rigth, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_rigth = pygame.transform.scale(atom_H_rigth, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_left = pygame.image.load("assets/sprites/H_left.png")
atom_H_left = pygame.transform.scale(atom_H_left, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_left = pygame.transform.scale(atom_H_left, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_up = pygame.image.load("assets/sprites/H_up.png")
atom_H_up = pygame.transform.scale(atom_H_up, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_up = pygame.transform.scale(atom_H_up, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_down = pygame.image.load("assets/sprites/H_down.png")
atom_H_down = pygame.transform.scale(atom_H_down, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_down = pygame.transform.scale(atom_H_down, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_diagonal_down_left = pygame.image.load("assets/sprites/H_diagonal_down_left.png")
atom_H_diagonal_down_left = pygame.transform.scale(atom_H_diagonal_down_left, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_diagonal_down_left = pygame.transform.scale(atom_H_diagonal_down_left, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_diagonal_up_left = pygame.image.load("assets/sprites/H_diagonal_up_left.png")
atom_H_diagonal_up_left = pygame.transform.scale(atom_H_diagonal_up_left, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_diagonal_up_left = pygame.transform.scale(atom_H_diagonal_up_left, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_diagonal_down_right = pygame.image.load("assets/sprites/H_diagonal_down_right.png")
atom_H_diagonal_down_right = pygame.transform.scale(atom_H_diagonal_down_right, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_diagonal_down_right = pygame.transform.scale(atom_H_diagonal_down_right, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_H_diagonal_up_right = pygame.image.load("assets/sprites/H_diagonal_up_right.png")
atom_H_diagonal_up_right = pygame.transform.scale(atom_H_diagonal_up_right, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_H_diagonal_up_right = pygame.transform.scale(atom_H_diagonal_up_right, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

# Oxigen

atom_O_left_rigth = pygame.image.load("assets/sprites/O_left_right.png")
atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_O_up_down = pygame.image.load("assets/sprites/O_up_down.png")
atom_O_up_down = pygame.transform.scale(atom_O_up_down, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_O_up_down = pygame.transform.scale(atom_O_up_down, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_O_double_left = pygame.image.load("assets/sprites/O_double_left.png")
atom_O_double_left = pygame.transform.scale(atom_O_double_left, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_O_double_left= pygame.transform.scale(atom_O_double_left, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_O_double_up= pygame.image.load("assets/sprites/O_double_up.png")
atom_O_double_up = pygame.transform.scale(atom_O_double_up, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_O_double_up = pygame.transform.scale(atom_O_double_up, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

# Carbon

atom_C_cross = pygame.image.load("assets/sprites/C_cross.png")
atom_C_cross = pygame.transform.scale(atom_C_cross, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_C_cross = pygame.transform.scale(atom_C_cross, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_C_double_down = pygame.image.load("assets/sprites/C_double_down.png")
atom_C_double_down = pygame.transform.scale(atom_C_double_down, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_C_double_down = pygame.transform.scale(atom_C_double_down, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_C_right_diagonal = pygame.image.load("assets/sprites/C_double_right_diagonal.png")
atom_C_right_diagonal = pygame.transform.scale(atom_C_right_diagonal, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_C_right_diagonal = pygame.transform.scale(atom_C_right_diagonal, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_C_double_left_diagonal = pygame.image.load("assets/sprites/C_double_left_diagonal.png")
atom_C_double_left_diagonal = pygame.transform.scale(atom_C_double_left_diagonal, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_C_double_left_diagonal = pygame.transform.scale(atom_C_double_left_diagonal, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

atom_C_double_right = pygame.image.load("assets/sprites/C_double_right.png")
atom_C_double_right = pygame.transform.scale(atom_C_double_right, (SQUARE_SIZE, SQUARE_SIZE))
molecule_atom_C_double_right = pygame.transform.scale(atom_C_double_right, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

# Bottles

bottle_0 = pygame.image.load("assets/sprites/bottle_0.png")
bottle_0 = pygame.transform.scale(bottle_0, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_0 = pygame.transform.scale(bottle_0, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_1 = pygame.image.load("assets/sprites/bottle_1.png")
bottle_1 = pygame.transform.scale(bottle_1, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_1 = pygame.transform.scale(bottle_1, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_2 = pygame.image.load("assets/sprites/bottle_2.png")
bottle_2 = pygame.transform.scale(bottle_2, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_2 = pygame.transform.scale(bottle_2, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_3 = pygame.image.load("assets/sprites/bottle_3.png")
bottle_3 = pygame.transform.scale(bottle_3, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_3 = pygame.transform.scale(bottle_3, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_4 = pygame.image.load("assets/sprites/bottle_4.png")
bottle_4 = pygame.transform.scale(bottle_4, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_4 = pygame.transform.scale(bottle_4, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_5 = pygame.image.load("assets/sprites/bottle_5.png")
bottle_5 = pygame.transform.scale(bottle_5, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_5 = pygame.transform.scale(bottle_5, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_6 = pygame.image.load("assets/sprites/bottle_6.png")
bottle_6 = pygame.transform.scale(bottle_6, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_6 = pygame.transform.scale(bottle_6, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

bottle_7 = pygame.image.load("assets/sprites/bottle_7.png")
bottle_7 = pygame.transform.scale(bottle_7, (SQUARE_SIZE, SQUARE_SIZE))
molecule_bottle_7 = pygame.transform.scale(bottle_7, (MOLECULE_SQUARE_SIZE, MOLECULE_SQUARE_SIZE))

# Players

players = ["PLAYER 1", "GREEDY", "BFS", "A-STAR", "IDFS"]

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
atoms_list_level_1 = [Atom(0,3,7), Atom(1,8,6), Atom(2,3,2)]

timeout_level_1 = 150

matrix_offset_x_level_1 = 320
matrix_offset_y_level_1 = 75
molecule_offset_x_level_1 = 88

background_window_level_1 = "#2F2D29"
background_matrix_level_1 = "#FFB562"

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
atoms_list_level_2 = [Atom(0,9,4), Atom(1,2,5), Atom(2,5,4), Atom(3,8,8), Atom(4,3,9)]

timeout_level_2 = 150

matrix_offset_x_level_2 = 320
matrix_offset_y_level_2 = 75
molecule_offset_x_level_2 = 88

background_window_level_2 = "#2F2D29"
background_matrix_level_2 = "#FFB562"

sprites_level_2 = [atom_H_down, atom_H_rigth, atom_C_cross, atom_H_left, atom_H_up]
molecule_sprites_level_2 = [molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_H_left, molecule_atom_H_up]

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

atoms_list_level_3 = [Atom(0,2,3), Atom(1,2,8), Atom(2,9,7), Atom(3,6,8), Atom(4,8,10), Atom(5,5,10)]

timeout_level_3 = 150

matrix_offset_x_level_3 = 320
matrix_offset_y_level_3 = 75
molecule_offset_x_level_3 = 88

background_window_level_3 = "#2F2D29"
background_matrix_level_3 = "#FFB562"

sprites_level_3 = [atom_H_down, atom_H_rigth, atom_C_cross, atom_O_left_rigth, atom_H_left, atom_H_up]
molecule_sprites_level_3 = [molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_O_left_rigth, molecule_atom_H_left, molecule_atom_H_up]

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
                    [-1, 2, 3,-1],
                    [ 4,-1,-1, 5]]

atoms_list_level_4 = [Atom(0,5,9), Atom(1,7,7), Atom(2,5,7), Atom(3,2,7), Atom(4,3,2), Atom(5,3,11)]

timeout_level_4 = 360

matrix_offset_x_level_4 = 320
matrix_offset_y_level_4 = 75
molecule_offset_x_level_4 = 88

background_window_level_4 = "#2F2D29"
background_matrix_level_4 = "#FFB562"

sprites_level_4 = [atom_H_diagonal_down_right, atom_H_diagonal_down_left, atom_C_right_diagonal, atom_C_double_left_diagonal, atom_H_diagonal_up_right, atom_H_diagonal_up_left]
molecule_sprites_level_4 = [molecule_atom_H_diagonal_down_right, molecule_atom_H_diagonal_down_left, molecule_atom_C_right_diagonal, molecule_atom_C_double_left_diagonal, molecule_atom_H_diagonal_up_right, molecule_atom_H_diagonal_up_left]

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

molecule_level_5 = [[-1, 0, 0,-1, 1],
                    [ 2, 3, 4, 5,-1],
                    [-1, 6,-1,-1, 7]]

atoms_list_level_5 = [Atom(0,5,3), Atom(0,10,7), Atom(1,8,2), Atom(2,3,6), Atom(3,8,6), Atom(4,3,4), Atom(5,11,5), Atom(6,9, 11), Atom(7,1,11)]

timeout_level_5 = 150

matrix_offset_x_level_5 = 320
matrix_offset_y_level_5 = 75
molecule_offset_x_level_5 = 88

background_window_level_5 = "#2F2D29"
background_matrix_level_5 = "#FFB562"

sprites_level_5 = [atom_H_down, atom_H_diagonal_down_left, atom_H_rigth, atom_C_cross, atom_C_double_right, atom_C_double_left_diagonal, atom_H_up, atom_H_diagonal_up_left, atom_H_diagonal_up_left]
molecule_sprites_level_5 = [molecule_atom_H_down, molecule_atom_H_diagonal_down_left, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_C_double_right, molecule_atom_C_double_left_diagonal, molecule_atom_H_up, molecule_atom_H_diagonal_up_left]

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

atoms_list_level_6 = [Atom(0,1,3), Atom(1,4,1), Atom(2,3,4), Atom(3,2,1), Atom(4,4,3), Atom(5,1,4), Atom(6,2,2), Atom(7,3,2)]

timeout_level_6 = 150

matrix_offset_x_level_6 = 320
matrix_offset_y_level_6 = 75
molecule_offset_x_level_6 = 88

background_window_level_6 = "#404B5B"
background_matrix_level_6 = "#F0F7EE"

sprites_level_6 = [bottle_0, bottle_1, bottle_2, bottle_3, bottle_4, bottle_5, bottle_6, bottle_7]
molecule_sprites_level_6 = [molecule_bottle_0, molecule_bottle_1, molecule_bottle_2, molecule_bottle_3, molecule_bottle_4, molecule_bottle_5, molecule_bottle_6, molecule_bottle_7]

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

molecule_level_7 = [[-1, 0, 0,-1,-1],
                    [ 1, 2, 2, 3, 4],
                    [-1, 5, 5,-1,-1]]

atoms_list_level_7 = [Atom(0,3,1), Atom(0,9,9), Atom(1,2,9), Atom(2,6,3), Atom(2,8,5), Atom(3,5,8), Atom(4,3,5), Atom(5,6,10), Atom(5,4,11)]

timeout_level_7 = 150

matrix_offset_x_level_7 = 320
matrix_offset_y_level_7 = 75
molecule_offset_x_level_7 = 88

background_window_level_7 = "#2F2D29"
background_matrix_level_7 = "#FFB562"

sprites_level_7 = [ atom_H_down, atom_H_down, atom_H_rigth, atom_C_cross, atom_C_cross, atom_O_left_rigth, atom_H_left, atom_H_up, atom_H_up]
molecule_sprites_level_7 = [ molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_O_left_rigth, molecule_atom_H_left, molecule_atom_H_up, molecule_atom_H_up, molecule_atom_H_up]

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

molecule_level_8 = [[-1, 0, 0, 0,-1],
                    [ 1, 2, 2, 2, 3],
                    [-1, 4, 5, 4,-1],
                    [-1,-1, 4,-1,-1]]

atoms_list_level_8 = [Atom(0,8,1), Atom(0,2,4), Atom(0,9,7), Atom(1,3,10), Atom(2,2,8), Atom(2,7,10), Atom(2,9,5), Atom(3,9,9), Atom(4,4,4), Atom(5,6,3), Atom(4,7,5), Atom(4,7,9)]

timeout_level_8 = 150

matrix_offset_x_level_8 = 320
matrix_offset_y_level_8 = 75
molecule_offset_x_level_8 = 88

background_window_level_8 = "#2F2D29"
background_matrix_level_8 = "#FFB562"

sprites_level_8 = [atom_H_down, atom_H_down, atom_H_down, atom_H_rigth, atom_C_cross,  atom_C_cross, atom_C_cross, atom_H_left, atom_H_up, atom_O_up_down, atom_H_up, atom_H_up]
molecule_sprites_level_8 = [molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_H_left, molecule_atom_H_up, molecule_atom_O_up_down, molecule_atom_H_up]

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

molecule_level_9 = [[-1, 0, 0,-1],
                    [ 1, 2, 3, 4],
                    [-1, 5,-1,-1]]

atoms_list_level_9 = [Atom(0,8,5), Atom(0,6,3), Atom(1,2,5), Atom(2,6,4), Atom(3,4,7), Atom(4,7,1), Atom(5,5,5)]

timeout_level_9 = 150

matrix_offset_x_level_9 = 320
matrix_offset_y_level_9 = 75
molecule_offset_x_level_9 = 88

background_window_level_9 = "#2F2D29"
background_matrix_level_9 = "#FFB562"

sprites_level_9 = [atom_H_down, atom_H_down, atom_H_rigth, atom_C_cross, atom_C_double_right, atom_O_double_left, atom_H_up]
molecule_sprites_level_9 = [molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_C_double_right, molecule_atom_O_double_left, molecule_atom_H_up]

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

molecule_level_10 = [[-1, 0,-1, 0,-1],
                     [ 1, 2, 3, 2, 4],
                     [-1, 5, 6, 5,-1]]

atoms_list_level_10 = [Atom(0,7,3), Atom(0,9,5), Atom(1,4,9), Atom(2,6,7), Atom(3,8,7), Atom(2,10,5), Atom(4,9,2), Atom(5,3,1), Atom(6,9,8), Atom(5,3,3)]

timeout_level_10 = 150

matrix_offset_x_level_10 = 320
matrix_offset_y_level_10 = 75
molecule_offset_x_level_10 = 88

background_window_level_10 = "#2F2D29"
background_matrix_level_10 = "#FFB562"

sprites_level_10 = [atom_H_down, atom_H_down, atom_H_rigth, atom_C_cross, atom_C_double_down, atom_C_cross, atom_H_left, atom_H_up, atom_O_double_up, atom_H_up]
molecule_sprites_level_10 = [molecule_atom_H_down, molecule_atom_H_rigth, molecule_atom_C_cross, molecule_atom_C_double_down, molecule_atom_H_left, molecule_atom_H_up, molecule_atom_O_double_up]

# Levels list
level_1 = Level(1, matrix_level_1, molecule_level_1, atoms_list_level_1, timeout_level_1, sprites_level_1, molecule_sprites_level_1, matrix_offset_x_level_1, matrix_offset_y_level_1, molecule_offset_x_level_1, background_window_level_1, background_matrix_level_1)
level_2 = Level(2, matrix_level_2, molecule_level_2, atoms_list_level_2, timeout_level_2, sprites_level_2, molecule_sprites_level_2, matrix_offset_x_level_2, matrix_offset_y_level_2, molecule_offset_x_level_2, background_window_level_2, background_matrix_level_2)
level_3 = Level(3, matrix_level_3, molecule_level_3, atoms_list_level_3, timeout_level_3, sprites_level_3, molecule_sprites_level_3, matrix_offset_x_level_3, matrix_offset_y_level_3, molecule_offset_x_level_3, background_window_level_3, background_matrix_level_3)
level_4 = Level(4, matrix_level_4, molecule_level_4, atoms_list_level_4, timeout_level_4, sprites_level_4, molecule_sprites_level_4, matrix_offset_x_level_4, matrix_offset_y_level_4, molecule_offset_x_level_4, background_window_level_4, background_matrix_level_4)
level_5 = Level(5, matrix_level_5, molecule_level_5, atoms_list_level_5, timeout_level_5, sprites_level_5, molecule_sprites_level_5, matrix_offset_x_level_5, matrix_offset_y_level_5, molecule_offset_x_level_5, background_window_level_5, background_matrix_level_5)
level_6 = Level(6, matrix_level_6, molecule_level_6, atoms_list_level_6, timeout_level_6, sprites_level_6, molecule_sprites_level_6, matrix_offset_x_level_6, matrix_offset_y_level_6, molecule_offset_x_level_6, background_window_level_6, background_matrix_level_6)
level_7 = Level(7, matrix_level_7, molecule_level_7, atoms_list_level_7, timeout_level_7, sprites_level_7, molecule_sprites_level_7, matrix_offset_x_level_7, matrix_offset_y_level_7, molecule_offset_x_level_7, background_window_level_7, background_matrix_level_7)
level_8 = Level(8, matrix_level_8, molecule_level_8, atoms_list_level_8, timeout_level_8, sprites_level_8, molecule_sprites_level_8, matrix_offset_x_level_8, matrix_offset_y_level_8, molecule_offset_x_level_8, background_window_level_8, background_matrix_level_8)
level_9 = Level(9, matrix_level_9, molecule_level_9, atoms_list_level_9, timeout_level_9, sprites_level_9, molecule_sprites_level_9, matrix_offset_x_level_9, matrix_offset_y_level_9, molecule_offset_x_level_9, background_window_level_1, background_matrix_level_9)
level_10 = Level(10, matrix_level_10, molecule_level_10, atoms_list_level_10, timeout_level_10, sprites_level_10, molecule_sprites_level_10, matrix_offset_x_level_10, matrix_offset_y_level_10, molecule_offset_x_level_10, background_window_level_10, background_matrix_level_10)

levels = [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10] 

