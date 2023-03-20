
def winning_state(level, molecule, list_atoms):
    curx = list_atoms[0].get_x()
    cury = list_atoms[0].get_y()
    natoms = 0

    for k in range(0, len(molecule[0])):
        if molecule[0][k] == 1:
            curx = curx - k

    for y in range(0, len(molecule[0])):
        for x in range(0, len(molecule)):
            if molecule[x][y] != 0:
                if level[x + curx][y + cury] == molecule[x][y]:
                    natoms = natoms + 1
    
    if natoms == len(list_atoms):
        return True
    else:
        False
    

