def objective_test(level_matrix, atoms_list, molecule):
    atom_index = 0

    while atoms_list[atom_index].id == 0:
        # Link molecule positions to state positions
        current_x = atoms_list[atom_index].x - molecule[0].index(0)
        current_y = atoms_list[atom_index].y
        
        nr_correct_atoms = 0

        for y in range(0, len(molecule)):
            for x in range(0, len(molecule[y])):
                if molecule[y][x] >= 0:
                    # Prevent out of range indexes
                    if (len(level_matrix[0]) <= (x + current_x)) or (len(level_matrix) <= (y + current_y)):
                        break
                    # Verify if the atom is in its correct position in the molecule
                    if atoms_list[molecule[y][x]].x == x + current_x and atoms_list[molecule[y][x]].y == y + current_y:
                        nr_correct_atoms += 1
            else:
                continue
            break
                        
        if nr_correct_atoms == len(atoms_list):
            return True
        
        atom_index += 1

    return False
