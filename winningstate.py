
def winning_state(level, molecule, list_atoms):
    curx = list_atoms[0].get_x()
    cury = list_atoms[0].get_y()
    natoms = 0

    for k in range(0, len(molecule[0])):
        if molecule[0][k] == 1:
            curx = curx - k

    for y in range(0, len(molecule)):
        for x in range(0, len(molecule[y])):
            if molecule[y][x] > 0:
                if (len(level[0]) <= (x + curx)) or (len(level) <= (y + cury)):
                    return False;
            
                if level[y + cury][x + curx] == molecule[y][x]:
                    natoms = natoms + 1
                    
    
    if natoms == len(list_atoms):
        print("WIN")
        return True
    else:
        return False
    