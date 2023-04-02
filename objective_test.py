import numpy as np
import time
from data_levels import atoms_list_level_1


def objective_test(level_matrix, atoms_list, molecule):
    # Link molecule positions to state positions
    current_x = atoms_list[0][0] - molecule[0].index(0)
    current_y = atoms_list[0][1]
    
    nr_correct_atoms = 0

    for y in range(0, len(molecule)):
        for x in range(0, len(molecule[y])):
            if molecule[y][x] >= 0:
                # Prevent out of range indexes
                if (len(level_matrix[0]) <= (x + current_x)) or (len(level_matrix) <= (y + current_y)):
                    return False
                # Verify if the atom is in its correct position in the molecule
                if atoms_list[molecule[y][x]][0] == x + current_x and atoms_list[molecule[y][x]][1] == y + current_y:
                    nr_correct_atoms += 1
                    
    if nr_correct_atoms == len(atoms_list):
        return True
    else:
        return False
