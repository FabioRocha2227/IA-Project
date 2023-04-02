import pygame


SQUARE_SIZE = 32
MOLECULE_SQUARE_SIZE = 16

RIGTH_OFFSET = 320
DOWN_OFFSET = 75

TEXT_COLOR = "white"
TEXT_ALERT_COLOR = "red"

menu_initial_background = "#E2C580"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Atomix (Group 86)')
clock = pygame.time.Clock()

# Text
#font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.SysFont(",", 18)
font_molecule_name = pygame.font.SysFont(",", 14)
font_level_timeout = pygame.font.SysFont(",", 48)
font_menu_10 = pygame.font.Font("assets/fonts/Boeing.ttf", 10)
font_menu_14 = pygame.font.Font("assets/fonts/Boeing.ttf", 14)
font_menu_16 = pygame.font.Font("assets/fonts/Boeing.ttf", 16)
font_menu_22 = pygame.font.Font("assets/fonts/Boeing.ttf", 22)
font_menu_26 = pygame.font.Font("assets/fonts/Boeing.ttf", 26)
font_menu_36 = pygame.font.Font("assets/fonts/Boeing.ttf", 36)
font_verdana_10 = pygame.font.SysFont("Verdana", 10)
game_text_score = ["PLAYER 1", "HIGHSCORE"]
game_text_level = ["LEVEL", "TIME"]

# Timer
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , 1000)
