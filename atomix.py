import pygame
from data_levels import levels
from game import play
from algorithm_BFS import breadth_first_search
from algorithm_IDFS import iterative_deepening_search
from objective_test import objective_test
import numpy as np
from utils_algorithms import print_solution

level = levels[0]



""" goal = iterative_deepening_search(level, 5)
print_solution(goal) """

""" goal = breadth_first_search(level)
print_solution(goal) """

#while menu() > 0:
play(level)

pygame.quit()