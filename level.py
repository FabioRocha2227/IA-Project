
class Level():
    
    def __init__(self, initial_state, molecule, total_atoms, timeout, sprites, background_window, background_state):
        self.state = initial_state.copy()
        self.molecule = molecule
        self.total_atoms = total_atoms
        self.timeout = timeout
        self.sprites = sprites
        self.background_window = background_window
        self.background_state = background_state
        
        self.selected_atom = 1
        self.is_atom_picked = False
    