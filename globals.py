import pygame


SQUARE_SIZE = 32

RIGTH_OFFSET = 320
DOWN_OFFSET = 75

TEXT_COLOR = "white"
TEXT_ALERT_COLOR = "red"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Atomix (Group 86)')
clock = pygame.time.Clock()

# Text
#font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.SysFont(",", 18)
font_level_timeout = pygame.font.SysFont(",", 48)
game_text_score = ["PLAYER 1", "HIGHSCORE"]
game_text_level = ["LEVEL", "TIME"]

# Timer
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , 1000)
