
class Level():
    
    def __init__(self, matrix, molecule, atoms_list, timeout, sprites, background_window, background_matrix):
        self.matrix = matrix
        self.molecule = molecule
        self.atoms_list = atoms_list
        self.timeout = timeout
        self.sprites = sprites
        self.background_window = background_window
        self.background_matrix = background_matrix
        
        self.selected_atom = 1
        self.is_atom_picked = False
    