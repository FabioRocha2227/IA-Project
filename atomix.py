import pygame
from data import levels
from game import menu
from algorithm_BFS import breadth_first_search
from algorithm_IDFS import iterative_deepening_search
from algorithm_greedy import greedy_best_first_search
from algorithm_A_star import a_star
from objective_test import *
import numpy as np
from utils_algorithms import print_solution
from evaluation_function import *
from atom import *
""" 
level = levels[7]

molecule_level_8 = [[-1, 0, 0, 0,-1],
                    [ 1, 2, 2, 2, 3],
                    [-1, 4, 5, 4,-1],
                    [-1,-1, 4,-1,-1]]

atoms_list = [Atom(0,3,3), Atom(0,4,3), Atom(0,5,3), Atom(1,2,4), Atom(2,4,4), Atom(2,3,4), Atom(2,5,4), Atom(3,7,4), Atom(4,4,6), Atom(4,5,5), Atom(4,3,5), Atom(5,4,5)]

print(objective_test(level.matrix, atoms_list, level.molecule))
 """

""" goal = iterative_deepening_search(level, 10)
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


""" molecule_level_2 = [[-1, 0,-1],
                    [ 1, 2, 3],
                    [-1, 4,-1]]
atoms_list = [[2,5], [1,6], [2,6], [3,6], [2,7]]

print(objective_test(level.matrix, atoms_list, molecule_level_2)) """


#menu()

from game import play
level = levels[9]
level.player = 0
play(level)

pygame.quit()
