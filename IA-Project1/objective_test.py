import copy

def objective_test(level_matrix, atoms_list, molecule):
    atom_index = 0

    while atoms_list[atom_index].id == 0:
        temp_atoms_list = copy.deepcopy(atoms_list)

        # Link molecule positions to state positions
        current_x = atoms_list[atom_index].x - molecule[0].index(0)
        current_y = atoms_list[atom_index].y

        for y in range(0, len(molecule)):
            for x in range(0, len(molecule[y])):
                if molecule[y][x] >= 0:
                    # Verify if the atom is in its correct position in the molecule
                    for atom in temp_atoms_list:
                        if atom.id == molecule[y][x]:
                            if atom.x == x + current_x and atom.y == y + current_y:
                                temp_atoms_list.remove(atom)
                        
        if len(temp_atoms_list) == 0:
            return True
        
        atom_index += 1

    return False
