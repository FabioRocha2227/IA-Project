import copy

def move_down(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom].x, atoms_list[selected_atom].y
  
  new_state = copy.deepcopy(atoms_list)

  max_y = len(level_matrix) - 1

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_x == atoms_list[i].x and selected_atom_y < atoms_list[i].y:
      if(atoms_list[i].y < max_y):
        max_y = atoms_list[i].y

  while selected_atom_y < max_y - 1 and level_matrix[selected_atom_y + 1][selected_atom_x] == 0:      
    selected_atom_y += 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state



def move_up(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom].x, atoms_list[selected_atom].y
  
  new_state = copy.deepcopy(atoms_list)

  min_y = 0

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_x == atoms_list[i].x and selected_atom_y > atoms_list[i].y:
      if(atoms_list[i].y > min_y):
        min_y = atoms_list[i].y

  while selected_atom_y > min_y + 1 and level_matrix[selected_atom_y - 1][selected_atom_x] == 0:      
    selected_atom_y -= 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state



def move_left(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom].x, atoms_list[selected_atom].y
  
  new_state = copy.deepcopy(atoms_list)

  min_x = 0

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_y == atoms_list[i].y and selected_atom_x > atoms_list[i].x:
      if(atoms_list[i].x > min_x):
        min_x = atoms_list[i].x

  while selected_atom_x > min_x + 1 and level_matrix[selected_atom_y][selected_atom_x - 1] == 0:      
    selected_atom_x -= 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state

      
            
def move_right(level_matrix, selected_atom, atoms_list):
  selected_atom_x, selected_atom_y = atoms_list[selected_atom].x, atoms_list[selected_atom].y
  
  new_state = copy.deepcopy(atoms_list)

  max_x = len(level_matrix[0]) - 1

  for i in range(0, len(atoms_list)):
    if selected_atom != i and selected_atom_y == atoms_list[i].y and selected_atom_x < atoms_list[i].x:
      if(atoms_list[i].x < max_x):
        max_x = atoms_list[i].x

  while selected_atom_x < max_x - 1 and level_matrix[selected_atom_y][selected_atom_x + 1] == 0:      
    selected_atom_x += 1

  new_state[selected_atom] = [selected_atom_x, selected_atom_y]
  
  return new_state
