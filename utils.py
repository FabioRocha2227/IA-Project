import numpy as np



def select_atom_up(state, selected_atom):
    selected_atom_index = np.where(state == selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_y > 1:
        for x in range(0, -len(state[0]), -1):
            x_offset = x

            if selected_atom_x + x_offset < 1 and x_offset != 0 and sides == 2:
                x_offset = abs(x_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    x_offset = abs(x_offset)

                if x_offset >= 0 and selected_atom_x + x_offset > len(state[0]) - 2:
                    sides = 1
                    break

                for y in range(selected_atom_y - 1, 0, -1):
                    if state[y][selected_atom_x + x_offset] < -1:
                        break
                    
                    if state[y][selected_atom_x + x_offset] > 0:
                        return state[y][selected_atom_x + x_offset]
                    
                if x_offset == 0:
                    break
    else:
        return selected_atom
    
    return selected_atom



def select_atom_down(state, selected_atom):
    selected_atom_index = np.where(state == selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    x_offset = 0
    sides = 2

    if selected_atom_y < len(state) - 2:
        for x in range(0, -len(state[0]), -1):
            x_offset = x

            if selected_atom_x + x_offset < 1 and x_offset != 0 and sides == 2:
                x_offset = abs(x_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    x_offset = abs(x_offset)

                if x_offset >= 0 and selected_atom_x + x_offset > len(state[0]) - 2:
                    sides = 1
                    break

                for y in range(selected_atom_y + 1, len(state)):
                    if state[y][selected_atom_x + x_offset] < -1:
                        break
                    
                    if state[y][selected_atom_x + x_offset] > 0:
                        return state[y][selected_atom_x + x_offset]
                    
                if x_offset == 0:
                    break
    else:
        return selected_atom
    
    return selected_atom



def select_atom_left(state, selected_atom):
    selected_atom_index = np.where(state == selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_x > 1:
        for y in range(0, -len(state), -1):
            y_offset = y

            if selected_atom_y + y_offset < 1 and y_offset != 0 and sides == 2:
                y_offset = abs(y_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    y_offset = abs(y_offset)

                if y_offset >= 0 and selected_atom_y + y_offset > len(state) - 2:
                    sides = 1
                    break

                for x in range(selected_atom_x - 1, 0, -1):
                    if state[selected_atom_y + y_offset][x] < -1:
                        break
                    
                    if state[selected_atom_y + y_offset][x] > 0:
                        return state[selected_atom_y + y_offset][x]
                    
                if y_offset == 0:
                    break
    else:
        return selected_atom
    
    return selected_atom



def select_atom_right(state, selected_atom):
    selected_atom_index = np.where(state == selected_atom)
    selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

    sides = 2

    if selected_atom_x < len(state[0]) - 2:
        for y in range(0, -len(state), -1):
            y_offset = y

            if selected_atom_y + y_offset < 1 and y_offset != 0 and sides == 2:
                y_offset = abs(y_offset)
                sides = 1

            for i in range(0, sides):
                if i == 1:
                    y_offset = abs(y_offset)

                if y_offset >= 0 and selected_atom_y + y_offset > len(state) - 2:
                    sides = 1
                    break
                
                for x in range(selected_atom_x + 1, len(state[0])):
                    if state[selected_atom_y + y_offset][x] < -1:
                        break
                    
                    if state[selected_atom_y + y_offset][x] > 0:
                        return state[selected_atom_y + y_offset][x]
                    
                if y_offset == 0:
                    break
    else:
        return selected_atom
    
    return selected_atom
