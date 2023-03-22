import numpy as np
import time
from data_levels import total_atoms_level_1



def objective_test(level_state, molecule):
    # Link molecule positions to state positions
    atom_id_1 = np.where(level_state == 1)
    current_x, current_y = atom_id_1[1][0], atom_id_1[0][0]
    current_x = current_x - molecule[0].index(1)
    
    nr_correct_atoms = 0

    for y in range(0, len(molecule)):
        for x in range(0, len(molecule[y])):
            if molecule[y][x] > 0:
                # Prevent out of range indexes
                if (len(level_state[0]) <= (x + current_x)) or (len(level_state) <= (y + current_y)):
                    return False
                # Verify if the atom is in its correct position in the molecule
                if level_state[y + current_y][x + current_x] == molecule[y][x]:
                    nr_correct_atoms += 1
                    
    if nr_correct_atoms == total_atoms_level_1:
        print("WIN")
        time.sleep(1.5)
        return True
    else:
        return False
