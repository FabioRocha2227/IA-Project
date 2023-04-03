
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

""" def evaluate_links_and_distances(level_matrix, atoms_list, molecule):
    return evaluate_missing_links(level_matrix, atoms_list, molecule) * evaluate_distances(atoms_list) """
