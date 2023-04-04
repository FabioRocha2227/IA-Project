
def select_atom_up(level):
    selected_y = level.atoms_list[level.selected_atom].y

    atoms_up = []
    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].y < selected_y:
            atoms_up.append(i)

    nearest_x = len(level.matrix[0])
    atoms_nearest_x = []

    for i in range(len(atoms_up)):
        if abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_up[i]].x) < nearest_x:
            atoms_nearest_x = [atoms_up[i]]
            nearest_x = abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_up[i]].x)
        elif abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_up[i]].x) < nearest_x:
            atoms_nearest_x.append(atoms_up[i])

    nearest_y = 0

    for i in range(len(atoms_nearest_x)):
        if level.atoms_list[atoms_nearest_x[i]].y > nearest_y:
                nearest_y = level.atoms_list[atoms_nearest_x[i]].y
                level.selected_atom = atoms_nearest_x[i]



def select_atom_down(level):
    selected_y = level.atoms_list[level.selected_atom].y

    atoms_down = []
    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].y > selected_y:
            atoms_down.append(i)

    nearest_x = len(level.matrix[0])
    atoms_nearest_x = []

    for i in range(len(atoms_down)):
        if abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_down[i]].x) < nearest_x:
            atoms_nearest_x = [atoms_down[i]]
            nearest_x = abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_down[i]].x)
        elif abs(level.atoms_list[level.selected_atom].x - level.atoms_list[atoms_down[i]].x) < nearest_x:
            atoms_nearest_x.append(atoms_down[i])

    nearest_y = len(level.matrix)

    for i in range(len(atoms_nearest_x)):
        if level.atoms_list[atoms_nearest_x[i]].y < nearest_y:
                nearest_y = level.atoms_list[atoms_nearest_x[i]].y
                level.selected_atom = atoms_nearest_x[i]



def select_atom_left(level):
    selected_x = level.atoms_list[level.selected_atom].x

    atoms_left = []
    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].x < selected_x:
            atoms_left.append(i)

    nearest_y = len(level.matrix)
    atoms_nearest_y = []

    for i in range(len(atoms_left)):
        if abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_left[i]].y) < nearest_y:
            atoms_nearest_y = [atoms_left[i]]
            nearest_y = abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_left[i]].y)
        elif abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_left[i]].y) < nearest_y:
            atoms_nearest_y.append(atoms_left[i])

    nearest_x = 0

    for i in range(len(atoms_nearest_y)):
        if level.atoms_list[atoms_nearest_y[i]].x > nearest_x:
                nearest_x = level.atoms_list[atoms_nearest_y[i]].x
                level.selected_atom = atoms_nearest_y[i]



def select_atom_right(level):
    selected_x = level.atoms_list[level.selected_atom].x

    atoms_right = []
    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].x > selected_x:
            atoms_right.append(i)

    nearest_y = len(level.matrix)
    atoms_nearest_y = []

    for i in range(len(atoms_right)):
        if abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_right[i]].y) < nearest_y:
            atoms_nearest_y = [atoms_right[i]]
            nearest_y = abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_right[i]].y)
        elif abs(level.atoms_list[level.selected_atom].y - level.atoms_list[atoms_right[i]].y) < nearest_y:
            atoms_nearest_y.append(atoms_right[i])

    nearest_x = len(level.matrix[0])

    for i in range(len(atoms_nearest_y)):
        if level.atoms_list[atoms_nearest_y[i]].x < nearest_x:
                nearest_x = level.atoms_list[atoms_nearest_y[i]].x
                level.selected_atom = atoms_nearest_y[i]
