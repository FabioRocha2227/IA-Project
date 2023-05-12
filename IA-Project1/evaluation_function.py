def evaluate_distances(atoms_list):
    distances = 0
    next_atom = 0
    for i in range(0, len(atoms_list) - 1):
        while True:
            next_atom += 1
            if next_atom >= len(atoms_list):
                next_atom = i
                break
            distances += atoms_list[i] - atoms_list[next_atom]

    return distances



def evaluate_missing_links(level_matrix, atoms_list, molecule):
    # Link molecule positions to state positions
    current_x = atoms_list[0].x - molecule[0].index(0)
    current_y = atoms_list[0].y
    
    nr_missing_links = len(atoms_list) -1

    for y in range(0, len(molecule)):
        for x in range(0, len(molecule[y])):
            if molecule[y][x] > 0:
                # Prevent out of range indexes
                if (len(level_matrix[0]) <= (x + current_x)) or (len(level_matrix) <= (y + current_y)):
                    return False
                # Verify if the atom is in its correct position in the molecule
                if atoms_list[molecule[y][x]].x == x + current_x and atoms_list[molecule[y][x]].y == y + current_y:
                    nr_missing_links -= 1
                else:
                    current_x = atoms_list[molecule[y][x]].x - x
                    current_y = atoms_list[molecule[y][x]].y - y

    return nr_missing_links



def evaluate_links_and_distances(level_matrix, atoms_list, molecule):
    return evaluate_missing_links(level_matrix, atoms_list, molecule) * evaluate_distances(atoms_list)
