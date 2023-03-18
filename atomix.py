# Example file showing a circle moving on screen
import pygame

board_level1 = [[-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 3,-1,-1,-1,-1,-1,-1, 0],
 [-1, 0, 0,-1, 0, 0, 0, 0, 0,-1, 0],
 [-1, 0,-1, 0, 0, 0, 0, 0, 0,-1,-1],
 [-1,0,-1,0,0,-1, 0,-1,-1, 0,-1],
 [-1, 0, 0, 0, 0,-1, 0,-1, 2, 0,-1],
 [-1,-1,-1, 1,-1, 0, 0,-1, 0, 0,-1],
 [0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
 [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]


class atom():
  
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
      
    def set_x(self, value):
        self.x = value
    
    def set_y(self, value):
        self.y = value

    def draw_atom(self):
        pygame.draw.circle(screen, "blue", pygame.Vector2(self.x*SQUARE_SIZE+RIGTH_OFFSET+30, self.y*SQUARE_SIZE+DOWN_OFFSET+30), 30)

atoms_list_level1 = [atom(3, 3, 2), atom(2, 8, 6), atom(1, 3, 7)]

        
      


SQUARE_SIZE = 60
RIGTH_OFFSET = 500
DOWN_OFFSET = 100

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# draw board
def draw_board(board):
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            if board[j][i] == -1:
                pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, "black", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 2)
            elif board[j][i] == 0:
                pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 2)

def draw_player_position(id, atom_list, picked_atom):
    color = "red"
    if picked_atom == True:
        color = "yellow"

    pygame.draw.rect(screen, color, pygame.Rect(atom_list[id].get_x()*SQUARE_SIZE+RIGTH_OFFSET, atom_list[id].get_y()*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 5)

#def move(direction):


# Level variables
board = board_level1
atoms_list = atoms_list_level1
selected_atom = 0
picked_atom = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if picked_atom == False:
                    picked_atom = True
                else:
                    picked_atom = False
            if picked_atom == False:
                if event.key == pygame.K_LEFT:
                    if selected_atom == 0:
                        selected_atom = len(atoms_list) - 1                 
                    else:
                        selected_atom = selected_atom - 1
                if event.key == pygame.K_RIGHT:
                    if selected_atom == len(atoms_list) - 1:
                        selected_atom = 0
                    else:
                        selected_atom = selected_atom + 1
            """else:
                if event.key == pygame.K_UP:
                if event.key == pygame.K_RIGHT:
                if event.key == pygame.K_DOWN:
                if event.key == pygame.K_LEFT:"""
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    draw_board(board_level1)

    draw_player_position(selected_atom, atoms_list, picked_atom)
    
    for atom_ in atoms_list:
        atom_.draw_atom()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()