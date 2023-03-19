import pygame
from globals import SQUARE_SIZE, RIGTH_OFFSET, DOWN_OFFSET, screen, clock

def draw_level(level):
    for i in range(0, len(level[0])):
        for j in range(0, len(level)):
            if level[j][i] == -1:
                pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, "black", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 2)
            elif level[j][i] == 0:
                pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 2)

def draw_player_position(id, atom_list, picked_atom):
    color = "red"
    if picked_atom == True:
        color = "yellow"
    pygame.draw.rect(screen, color, pygame.Rect(atom_list[id].get_x()*SQUARE_SIZE+RIGTH_OFFSET, atom_list[id].get_y()*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 5)

def draw_atom(atom_x):
    pygame.draw.circle(screen, "blue", pygame.Vector2(atom_x.x*SQUARE_SIZE+RIGTH_OFFSET+30, atom_x.y*SQUARE_SIZE+DOWN_OFFSET+30), 30)


def refresh():
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(15)
    
def draw(level, atoms_list, selected_atom, picked_atom, movement=False):  
 # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    draw_level(level)

    if not movement:
        draw_player_position(selected_atom, atoms_list, picked_atom)
    
    for atom_ in atoms_list:
        draw_atom(atom_)

    refresh()