from drawing import draw


# Coordinates madness
# Sei exatamente o que se está a passar 
def move_down(level, atoms_list, selected_atom):
  moving_atom = atoms_list[selected_atom]
  row = moving_atom.y
  col = moving_atom.x
  
  while row < len(level) - 1 and level[row + 1][col] == 0:
      tmp = level[row + 1][col]
      level[row + 1][col] = level[row][col]
      level[row][col] = tmp
      row += 1
      atoms_list[selected_atom].set_y(row)
      draw(level, atoms_list, selected_atom, True, movement=True)
      
      
def move_up(level, atoms_list, selected_atom):
  moving_atom = atoms_list[selected_atom]
  row = moving_atom.y
  col = moving_atom.x
  
  while row > 0 and level[row - 1][col] == 0:
      tmp = level[row - 1][col]
      level[row - 1][col] = level[row][col]
      level[row][col] = tmp
      row -= 1
      atoms_list[selected_atom].set_y(row)
      draw(level, atoms_list, selected_atom, True, movement=True)
   
      
def move_left(level, atoms_list, selected_atom):
  moving_atom = atoms_list[selected_atom]
  row = moving_atom.y
  col = moving_atom.x
  
  while col > 0 and level[row][col - 1] == 0:
      tmp = level[row][col - 1]
      level[row][col - 1] = level[row][col]
      level[row][col] = tmp
      col -= 1
      atoms_list[selected_atom].set_x(col)
      draw(level, atoms_list, selected_atom, True, movement=True)   
      
            
def move_right(level, atoms_list, selected_atom):
  moving_atom = atoms_list[selected_atom]
  row = moving_atom.y
  col = moving_atom.x
  
  while col < len(level[0]) - 1 and level[row][col + 1] == 0:
      tmp = level[row][col + 1]
      level[row][col + 1] = level[row][col]
      level[row][col] = tmp
      col += 1
      atoms_list[selected_atom].set_x(col)
      draw(level, atoms_list, selected_atom, True, movement=True)   
      
            





