import pygame
from data_levels import levels
from game import play
from algorithm_BFS import breadth_first_search
from algorithm_IDFS import iterative_deepening_search
from algorithm_greedy import greedy_best_first_search
from algorithm_A_star import a_star
from objective_test import objective_test, evaluate_missing_links
import numpy as np
from utils_algorithms import print_solution
from evaluation_function import *

level = levels[0]



""" goal = iterative_deepening_search(level, 5)
print_solution(goal) """

""" goal = breadth_first_search(level)
print_solution(goal) """

#m = evaluate_distances(level.atoms_list)
""" m = evaluate_missing_links(level.matrix, level.atoms_list, level.molecule)
print(m) """

""" goal = greedy_best_first_search(level)
print_solution(goal) """

""" goal = a_star(level)
print_solution(goal) """

#while menu() > 0:
play(level)

pygame.quit()