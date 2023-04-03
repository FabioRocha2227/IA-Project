from utils_algorithms import TreeNode, get_child_states
from objective_test import *
from evaluation_function import evaluate_distances, evaluate_links_and_distances
from queue import PriorityQueue


def greedy_best_first_search(level):
    start = TreeNode(level.atoms_list, heuristic=evaluate_links_and_distances(level.matrix, level.atoms_list, level.molecule))
    queue = PriorityQueue()
    queue.put((evaluate_links_and_distances(level.matrix, start.state, level.molecule), start))
    visited = []

    while not queue.empty():
        current = queue.get()[1]
        if objective_test(level.matrix, current.state, level.molecule):
            return current

        visited.append(current.state)
        for state in get_child_states(level.matrix, current.state):
            if state not in visited:
                child = TreeNode(state, heuristic=evaluate_links_and_distances(level.matrix, state, level.molecule), parent=current)
                current.add_child(child)
                queue.put((evaluate_links_and_distances(level.matrix, child.state, level.molecule), child))

    return None


'''Score = Nr of atoms not linked * Sum of all distances between atoms'''

