from drawing import draw
import numpy as np



def move_down(level_state, selected_atom):
  selected_atom_index = np.where(level_state == selected_atom)
  selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]
  
  new_state = level_state.copy()

  while selected_atom_y < len(new_state) - 1 and new_state[selected_atom_y + 1][selected_atom_x] == 0:
      tmp = new_state[selected_atom_y + 1][selected_atom_x]
      new_state[selected_atom_y + 1][selected_atom_x] = new_state[selected_atom_y][selected_atom_x]
      new_state[selected_atom_y][selected_atom_x] = tmp
      selected_atom_y += 1
      draw(new_state, selected_atom, True, movement=True)
  
  return new_state


 
def move_up(level_state, selected_atom):
  selected_atom_index = np.where(level_state == selected_atom)
  selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

  new_state = level_state.copy()
  
  while selected_atom_y > 0 and new_state[selected_atom_y - 1][selected_atom_x] == 0:
      tmp = new_state[selected_atom_y - 1][selected_atom_x]
      new_state[selected_atom_y - 1][selected_atom_x] = new_state[selected_atom_y][selected_atom_x]
      new_state[selected_atom_y][selected_atom_x] = tmp
      selected_atom_y -= 1
      draw(new_state, selected_atom, True, movement=True)

  return new_state



def move_left(level_state, selected_atom):
  selected_atom_index = np.where(level_state == selected_atom)
  selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

  new_state = level_state.copy()
  
  while selected_atom_x > 0 and new_state[selected_atom_y][selected_atom_x - 1] == 0:
      tmp = new_state[selected_atom_y][selected_atom_x - 1]
      new_state[selected_atom_y][selected_atom_x - 1] = new_state[selected_atom_y][selected_atom_x]
      new_state[selected_atom_y][selected_atom_x] = tmp
      selected_atom_x -= 1
      draw(new_state, selected_atom, True, movement=True)
  
  return new_state

      
            
def move_right(level_state, selected_atom):
  selected_atom_index = np.where(level_state == selected_atom)
  selected_atom_x, selected_atom_y = selected_atom_index[1][0], selected_atom_index[0][0]

  new_state = level_state.copy()
  
  while selected_atom_x < len(new_state[0]) - 1 and new_state[selected_atom_y][selected_atom_x + 1] == 0:
      tmp = new_state[selected_atom_y][selected_atom_x + 1]
      new_state[selected_atom_y][selected_atom_x + 1] = new_state[selected_atom_y][selected_atom_x]
      new_state[selected_atom_y][selected_atom_x] = tmp
      selected_atom_x += 1
      draw(new_state, selected_atom, True, movement=True)

  return new_state
