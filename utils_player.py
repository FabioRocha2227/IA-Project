
def select_atom_up(level):
    selected_y = level.atoms_list[level.selected_atom].y

    nearest_y = 0

    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].y < selected_y:
            if level.atoms_list[i].y > nearest_y:
                nearest_y = level.atoms_list[i].y
                level.selected_atom = i

def select_atom_down(level):
    selected_y = level.atoms_list[level.selected_atom].y

    nearest_y = len(level.matrix)

    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].y > selected_y:
            if level.atoms_list[i].y < nearest_y:
                nearest_y = level.atoms_list[i].y
                level.selected_atom = i

def select_atom_left(level):
    selected_x = level.atoms_list[level.selected_atom].x

    nearest_x = 0

    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].x < selected_x:
            if level.atoms_list[i].x > nearest_x:
                nearest_x = level.atoms_list[i].x
                level.selected_atom = i

def select_atom_right(level):
    selected_x = level.atoms_list[level.selected_atom].x

    nearest_x = len(level.matrix[0])

    for i in range(len(level.atoms_list)):
        if i != level.selected_atom and level.atoms_list[i].x > selected_x:
            if level.atoms_list[i].x < nearest_x:
                nearest_x = level.atoms_list[i].x
                level.selected_atom = i




""" import numpy as np



def select_atom_up(level):
    selected_atom_index = np.where(level.state == level.selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_y > 1:
        for x in range(0, -len(level.state[0]), -1):
            x_offset = x

            if selected_atom_x + x_offset < 1 and x_offset != 0 and sides == 2:
                x_offset = abs(x_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    x_offset = abs(x_offset)

                if x_offset >= 0 and selected_atom_x + x_offset > len(level.state[0]) - 2:
                    sides = 1
                    break

                for y in range(selected_atom_y - 1, 0, -1):
                    if level.state[y][selected_atom_x + x_offset] > 0:
                        level.selected_atom = level.state[y][selected_atom_x + x_offset]
                        return
                    
                if x_offset == 0:
                    break



def select_atom_down(level):
    selected_atom_index = np.where(level.state == level.selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    x_offset = 0
    sides = 2

    if selected_atom_y < len(level.state) - 2:
        for x in range(0, -len(level.state[0]), -1):
            x_offset = x

            if selected_atom_x + x_offset < 1 and x_offset != 0 and sides == 2:
                x_offset = abs(x_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    x_offset = abs(x_offset)

                if x_offset >= 0 and selected_atom_x + x_offset > len(level.state[0]) - 2:
                    sides = 1
                    break

                for y in range(selected_atom_y + 1, len(level.state)):
                    if level.state[y][selected_atom_x + x_offset] > 0:
                        level.selected_atom = level.state[y][selected_atom_x + x_offset]
                        return
                    
                if x_offset == 0:
                    break



def select_atom_left(level):
    selected_atom_index = np.where(level.state == level.selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_x > 1:
        for y in range(0, -len(level.state), -1):
            y_offset = y

            if selected_atom_y + y_offset < 1 and y_offset != 0 and sides == 2:
                y_offset = abs(y_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    y_offset = abs(y_offset)

                if y_offset >= 0 and selected_atom_y + y_offset > len(level.state) - 2:
                    sides = 1
                    break

                for x in range(selected_atom_x - 1, 0, -1):
                    if level.state[selected_atom_y + y_offset][x] > 0:
                        level.selected_atom = level.state[selected_atom_y + y_offset][x]
                        return
                    
                if y_offset == 0:
                    break



def select_atom_right(level):
    selected_atom_index = np.where(level.state == level.selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_x < len(level.state[0]) - 2:
        for y in range(0, -len(level.state), -1):
            y_offset = y

            if selected_atom_y + y_offset < 1 and y_offset != 0 and sides == 2:
                y_offset = abs(y_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    y_offset = abs(y_offset)

                if y_offset >= 0 and selected_atom_y + y_offset > len(level.state) - 2:
                    sides = 1
                    break
                
                for x in range(selected_atom_x + 1, len(level.state[0])):   
                    if level.state[selected_atom_y + y_offset][x] > 0:
                        level.selected_atom = level.state[selected_atom_y + y_offset][x]
                        return
                    
                if y_offset == 0:
                    break
 """