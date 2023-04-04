class Level():
    
    def __init__(self, id, matrix, molecule, atoms_list, timeout, sprites, molecule_sprites, matrix_offset_x, matrix_offset_y, molecule_offset_x, molecule_name_offset_x, background_window, background_matrix):
        self.id = id
        self.matrix = matrix
        self.molecule = molecule
        self.atoms_list = atoms_list
        self.timeout = timeout
        self.sprites = sprites
        self.molecule_sprites = molecule_sprites
        self.matrix_offset_x = matrix_offset_x
        self.matrix_offset_y = matrix_offset_y
        self.molecule_offset_x = molecule_offset_x
        self.molecule_name_offset_x = molecule_name_offset_x
        self.background_window = background_window
        self.background_matrix = background_matrix
        
        self.player = 0
        self.algorithm_moves = 0
        self.algorithm_time = 0
        self.selected_atom = 0
        self.is_atom_picked = False
