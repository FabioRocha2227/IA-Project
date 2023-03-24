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

initial_state_level_1 = np.array([[-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 0,-2,-3,-3,-3,-3,-3,-3],
                    [-2, 0, 0, 3,-2,-2,-2,-2,-2,-2,-3],
                    [-2, 0, 0,-1, 0, 0, 0, 0, 0,-2,-3],
                    [-2, 0,-1, 0, 0, 0, 0, 0, 0,-2,-2],
                    [-2,0,-1,0,0,-1, 0,-1,-1, 0,-2],
                    [-2, 0, 0, 0, 0,-1, 0,-1, 2, 0,-2],
                    [-2,-2,-1, 1,-1, 0, 0,-1, 0, 0,-2],
                    [-3,-2, 0, 0, 0, 0, 0, 0, 0, 0,-2],
                    [-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]])

molecule_level_1 = [[1,2,3]]

total_atoms_level_1 = 3
timeout_level_1 = 120

background_window_level_1 = "#2F2D29"#F1DDBF"
background_state_level_1 = "#FFB562"

atom_H_rigth = pygame.image.load("sprites/H_right.png")
atom_H_rigth = pygame.transform.scale(atom_H_rigth, (SQUARE_SIZE, SQUARE_SIZE))

atom_O_left_rigth = pygame.image.load("sprites/O_left_right.png")
atom_O_left_rigth = pygame.transform.scale(atom_O_left_rigth, (SQUARE_SIZE, SQUARE_SIZE))

atom_H_left = pygame.image.load("sprites/H_left.png")
atom_H_left = pygame.transform.scale(atom_H_left, (SQUARE_SIZE, SQUARE_SIZE))

sprites_level_1 = [0, atom_H_rigth, atom_O_left_rigth, atom_H_left]

# Level 2


# Levels list
level_1 = Level(initial_state_level_1, molecule_level_1, total_atoms_level_1, timeout_level_1, sprites_level_1, background_window_level_1, background_state_level_1)

levels = [level_1]