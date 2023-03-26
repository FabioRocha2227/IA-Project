from drawing import draw
from data_levels import timeout_level_1



def move_down(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom][0], atoms_list[selected_atom][1]
  
  new_state = atoms_list.copy()

  max_y = len(level_matrix) - 1

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_x == atoms_list[i][0] and selected_atom_y < atoms_list[i][1]:
      if(atoms_list[i][1] < max_y):
        max_y = atoms_list[i][1]

  while selected_atom_y < max_y - 1 and level_matrix[selected_atom_y + 1][selected_atom_x] == 0:      
    selected_atom_y += 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state



def move_up(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom][0], atoms_list[selected_atom][1]
  
  new_state = atoms_list.copy()

  min_y = 0

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_x == atoms_list[i][0] and selected_atom_y > atoms_list[i][1]:
      if(atoms_list[i][1] > min_y):
        min_y = atoms_list[i][1]

  while selected_atom_y > min_y + 1 and level_matrix[selected_atom_y - 1][selected_atom_x] == 0:      
    selected_atom_y -= 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state



def move_left(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom][0], atoms_list[selected_atom][1]
  
  new_state = atoms_list.copy()

  min_x = 0

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_y == atoms_list[i][1] and selected_atom_x > atoms_list[i][0]:
      if(atoms_list[i][0] > min_x):
        min_x = atoms_list[i][0]

  while selected_atom_x > min_x + 1 and level_matrix[selected_atom_y][selected_atom_x - 1] == 0:      
    selected_atom_x -= 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state

      
            
def move_right(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom][0], atoms_list[selected_atom][1]
  
  new_state = atoms_list.copy()

  max_x = len(level_matrix[0]) - 1

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_y == atoms_list[i][1] and selected_atom_x < atoms_list[i][0]:
      if(atoms_list[i][0] < max_x):
        max_x = atoms_list[i][0]

  while selected_atom_x < max_x - 1 and level_matrix[selected_atom_y][selected_atom_x + 1] == 0:      
    selected_atom_x += 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state
