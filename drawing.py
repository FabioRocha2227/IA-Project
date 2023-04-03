import pygame
import time
from data import *
from data import screen, clock


def draw_menu_initial(option):
    screen.fill("#E2C580")
    screen.blit(atomix_logo, (20, 20))

    color_1 = "#4A4A4A"
    color_2 = "#4A4A4A"

    group = font_menu_22.render("3LEIC08 - Group 86", True, "#6C648C", None)
    screen.blit(group, (24, 305))
    subject = font_menu_16.render("ARTIFICIAL INTELLIGENCE", True, "#FFF4DA", None)
    screen.blit(subject, (30, 327)) 
    
    name_1 = font_menu_14.render("Fabio Rocha", True, color_1, None)
    screen.blit(name_1, (20, 370))
    up_1 = font_menu_10.render("2 0 2 0 0 5 4 7 8", True, color_2, None)
    screen.blit(up_1, (144, 372))
    
    name_2 = font_menu_14.render("Sofia Goncalves", True, color_1, None)
    screen.blit(name_2, (20, 410))
    up_2 = font_menu_10.render("2 0 2 0 0 5 8 4 5", True, color_2, None)
    screen.blit(up_2, (183, 412))

    name_3 = font_menu_14.render("Tiago Marques", True, color_1, None)
    screen.blit(name_3, (20, 450))
    up_3 = font_menu_10.render("2 0 17 0 4 7 3 3", True, color_2, None)
    screen.blit(up_3, (168, 452))

    button_color = "#4E4B53"
    button_border_color = "#2C2C39"
    button_text_color = "#E7D8B4"

    pygame.draw.rect(screen, button_color, pygame.Rect(400, 120, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(400, 220, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_text_color, pygame.Rect(400, 320, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(400, 120, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(400, 220, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(400, 320, 250, 60), 3, border_radius = 10)
    group = font_menu_22.render("PLAY", True, button_text_color, None)
    screen.blit(group, (489, 142))
    group = font_menu_22.render("INSTRUCTIONS", True, button_text_color, None)
    screen.blit(group, (434, 242))
    group = font_menu_22.render("EXIT", True, button_color, None)
    screen.blit(group, (495, 342))

    pygame.draw.rect(screen, "yellow", pygame.Rect(400, (option + 1) * 100 + 20, 250, 60), 5, border_radius = 10)

    refresh()



def draw_menu_player(menu_player, players):
    screen.fill("#222222")

    button_color = "#4E4B53"
    button_border_color = "#2C2C39"
    button_text_color = "#E7D8B4"

    group = font_menu_26.render("SELECT GAME MODE", True, "#6C648C", None)
    screen.blit(group, (250, 70))

    # Left
    pygame.draw.rect(screen, button_color, pygame.Rect(100, 160, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(100, 260, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(100, 360, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(100, 160, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(100, 260, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(100, 360, 250, 60), 3, border_radius = 10)
    # Right
    pygame.draw.rect(screen, button_color, pygame.Rect(450, 160, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(450, 260, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_text_color, pygame.Rect(450, 360, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(450, 160, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(450, 260, 250, 60), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(450, 360, 250, 60), 3, border_radius = 10)
    
    group = font_menu_22.render(players[0], True, button_text_color, None)
    screen.blit(group, (165, 182))
    group = font_menu_22.render(players[1], True, button_text_color, None)
    screen.blit(group, (524, 182))
    group = font_menu_22.render(players[2], True, button_text_color, None)
    screen.blit(group, (196, 282))
    group = font_menu_22.render(players[3], True, button_text_color, None)
    screen.blit(group, (529, 282))
    group = font_menu_22.render(players[4], True, button_text_color, None)
    screen.blit(group, (193, 382))
    group = font_menu_22.render("BACK", True, button_color, None)
    screen.blit(group, (539, 382))
    
    selected_x = 100
    selected_y = 160
    if menu_player % 2 != 0:
        selected_x = 450
    if menu_player > 1 and menu_player < 4:
        selected_y = 260
    if menu_player > 3:
        selected_y = 360

    pygame.draw.rect(screen, "yellow", pygame.Rect(selected_x, selected_y, 250, 60), 5, border_radius = 10)

    refresh()


def draw_menu_levels(menu_level):
    screen.fill("#222222")

    button_color = "#4E4B53"
    button_border_color = "#2C2C39"
    button_text_color = "#E7D8B4"

    group = font_menu_26.render("SELECT LEVEL", True, "#6C648C", None)
    screen.blit(group, (288, 70))

    # Up
    pygame.draw.rect(screen, button_color, pygame.Rect(100, 140, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(230, 140, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(360, 140, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(490, 140, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(620, 140, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(100, 140, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(230, 140, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(360, 140, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(490, 140, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(620, 140, 80, 80), 3, border_radius = 10)
    # Down
    pygame.draw.rect(screen, button_color, pygame.Rect(100, 245, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(230, 245, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(360, 245, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(490, 245, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_color, pygame.Rect(620, 245, 80, 80), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(100, 245, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(230, 245, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(360, 245, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(490, 245, 80, 80), 3, border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(620, 245, 80, 80), 3, border_radius = 10)


    #Back
    pygame.draw.rect(screen, button_text_color, pygame.Rect(275, 370, 250, 60), border_radius = 10)
    pygame.draw.rect(screen, button_border_color, pygame.Rect(275, 370, 250, 60), 3, border_radius = 10)

    level = font_menu_36.render("1", True, button_text_color, None)
    screen.blit(level, (127, 157))
    level = font_verdana_10.render("WATER", True, button_text_color, None)
    screen.blit(level, (122, 195))

    level = font_menu_36.render("2", True, button_text_color, None)
    screen.blit(level, (257, 157))
    level = font_verdana_10.render("METHANE", True, button_text_color, None)
    screen.blit(level, (246, 195))
    
    level = font_menu_36.render("3", True, button_text_color, None)
    screen.blit(level, (387, 157))
    level = font_verdana_10.render("METHANOL", True, button_text_color, None)
    screen.blit(level, (372, 195))

    level = font_menu_36.render("4", True, button_text_color, None)
    screen.blit(level, (517, 157))
    level = font_verdana_10.render("ETHENE", True, button_text_color, None)
    screen.blit(level, (510, 195))

    level = font_menu_36.render("5", True, button_text_color, None)
    screen.blit(level, (647, 157))
    level = font_verdana_10.render("PROPENE", True, button_text_color, None)
    screen.blit(level, (637, 195))
    
    
    level = font_menu_36.render("6", True, button_text_color, None)
    screen.blit(level, (126, 262))
    level = font_verdana_10.render("- BONUS -", True, button_text_color, None)
    screen.blit(level, (113, 300))

    level = font_menu_36.render("7", True, button_text_color, None)
    screen.blit(level, (257, 262))
    level = font_verdana_10.render("ETHANOL", True, button_text_color, None)
    screen.blit(level, (247, 300))

    level = font_menu_36.render("8", True, button_text_color, None)
    screen.blit(level, (387, 262))
    level = font_verdana_10.render("PROPANOL", True, button_text_color, None)
    screen.blit(level, (374, 300))

    level = font_menu_36.render("9", True, button_text_color, None)
    screen.blit(level, (517, 262))
    level = font_verdana_10.render("ETHANAL", True, button_text_color, None)
    screen.blit(level, (507, 300))

    level = font_menu_36.render("10", True, button_text_color, None)
    screen.blit(level, (631, 262))
    level = font_verdana_10.render("PROPANON", True, button_text_color, None)
    screen.blit(level, (632, 300))

    level = font_menu_22.render("BACK", True, button_color, None)
    screen.blit(level, (364, 392))
    
    selected_x = 100 
    selected_y = 140
    if menu_level < 5:
        selected_x += menu_level * 130
    if menu_level > 4 and menu_level < 10:
        selected_x += (menu_level - 5) * 130
        selected_y = 245

    if menu_level != 10:
        pygame.draw.rect(screen, "yellow", pygame.Rect(selected_x, selected_y, 80, 80), 5, border_radius = 10)
    else:
        pygame.draw.rect(screen, "yellow", pygame.Rect(275, 370, 250, 60), 5, border_radius = 10)

    refresh()


def draw_player_position(level):
    color = "red"
    if level.is_atom_picked == True:
        color = "yellow"
    pygame.draw.rect(screen, color, pygame.Rect(level.atoms_list[level.selected_atom].x * SQUARE_SIZE + RIGTH_OFFSET, level.atoms_list[level.selected_atom].y * SQUARE_SIZE + DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 3)



def draw_atoms(level, movement):
    for i in range(0, len(level.atoms_list)):
        if i == level.selected_atom and not movement:
            draw_player_position(level)
        screen.blit(level.sprites[i], (level.atoms_list[i].x * SQUARE_SIZE+RIGTH_OFFSET, level.atoms_list[i].y * SQUARE_SIZE+DOWN_OFFSET))



def draw_text():
    for i in range(0, 2):
        # Info about the player and the scores
        text = font.render(game_text_score[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, (i * 50 + 20)))

        # Info about the level and its timeout
        text = font.render(game_text_level[i], True, TEXT_COLOR, None)
        screen.blit(text, (50, ((i + 1) * 70 + 80)))

    # Current level
    text = font_level_timeout.render("1", True, TEXT_COLOR, None)
    screen.blit(text, (50, 170))



def draw_scores():
    level_score, highscore = 0, 0
    text = font.render(str(level_score), True, TEXT_COLOR, None)
    screen.blit(text, (50, 35))
    text = font.render(str(highscore), True, TEXT_COLOR, None)
    screen.blit(text, (50, 85))



def draw_timeout(level_timeout):
    minutes = level_timeout // 60
    seconds = level_timeout - minutes * 60
    timeout = str(minutes) + ":"
    if seconds == 0:
        timeout += "00"
    elif seconds > 0 and seconds < 10:
        timeout += "0" + str(seconds)
    else:
        timeout += str(seconds)

    color = TEXT_COLOR
    if level_timeout <= 10:
        color = TEXT_ALERT_COLOR

    text = font_level_timeout.render(timeout, True, color, None)
    screen.blit(text, (50, 240))



def draw_molecule(level):
    pygame.draw.rect(screen, "#1B1B1B", pygame.Rect(50, 300, 125, 150))
    pygame.draw.rect(screen, "#131313", pygame.Rect(50, 300, 125, 150), 3)
    pygame.draw.rect(screen, "#363636", pygame.Rect(53, 303, 120, 25))
    text = font.render("- MOLECULE -", True, "#9D9D9D", None)
    screen.blit(text, (72, 310))
    text = font_molecule_name.render("WATER", True, "#787878", None)
    screen.blit(text, (95, 335))
    for i in range(0, len(level.molecule)):
        for j in range(0, len(level.molecule[0])):
            screen.blit(level.molecule_sprites[level.molecule[i][j]], (88 + j * MOLECULE_SQUARE_SIZE, 355 + i * MOLECULE_SQUARE_SIZE))



def refresh():
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(15)
    


def draw(level, movement=False):  
    screen.fill(level.background_window)

    # Draw state
    for i in range(0, len(level.matrix[0])):
        for j in range(0, len(level.matrix)):
            if level.matrix[j][i] == -2:
                screen.blit(wall_extern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
                #pygame.draw.rect(screen, "gray", pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))
            elif level.matrix[j][i] == -1:
                screen.blit(wall_intern, (i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET))
            elif level.matrix[j][i] >= 0:
                pygame.draw.rect(screen, level.background_matrix, pygame.Rect(i*SQUARE_SIZE+RIGTH_OFFSET, j*SQUARE_SIZE+DOWN_OFFSET, SQUARE_SIZE, SQUARE_SIZE))

    draw_atoms(level, movement)
    draw_text()
    draw_scores()
    draw_timeout(level.timeout)
    draw_molecule(level)

    refresh()



def draw_movement(level, new_state):
    old_state_atom_x, old_state_atom_y = level.atoms_list[level.selected_atom].x, level.atoms_list[level.selected_atom].y
    new_state_atom_x, new_state_atom_y = new_state[level.selected_atom].x, new_state[level.selected_atom].y
    # Vertical direction
    while new_state_atom_y != old_state_atom_y:
        if old_state_atom_y > new_state_atom_y:
            old_state_atom_y -= 1
        else:
            old_state_atom_y += 1

        level.atoms_list[level.selected_atom].y = old_state_atom_y

        draw(level, movement=True)
     
    # Horizontal direction
    while new_state_atom_x != old_state_atom_x:
        if old_state_atom_x > new_state_atom_x:
            old_state_atom_x -= 1
        else:
            old_state_atom_x += 1

        level.atoms_list[level.selected_atom].x = old_state_atom_x

        draw(level, movement=True)



def draw_solution(level, solution):
    for i in range(1, len(solution)):
        for j in range(0, len(level.atoms_list)):
            if level.atoms_list[j] != solution[i].state[j]:
                level.selected_atom = j
                break
        draw_movement(level, solution[i].state)
        #time.sleep(0.5)
    