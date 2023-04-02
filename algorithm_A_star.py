from utils_algorithms import TreeNode, get_child_states
from evaluation_function import evaluate_distances
from objective_test import objective_test
from queue import PriorityQueue

#heuristic=evaluate_distances(level.atoms_list)

def a_star(level):
    frontier = PriorityQueue()
    root = TreeNode(level.atoms_list, cost=0, heuristic=evaluate_distances(level.atoms_list))
    frontier.put(root)
    visited = [root.state]

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        if objective_test(level.matrix, current_node.state, level.molecule):
            return current_node

        visited.append(current_state)

        for child_state in get_child_states(level.matrix, current_node.state):
            if child_state in visited:
                continue

            child_cost = current_node.cost + 1  # assuming edge cost of 1
            child_heuristic = evaluate_distances(child_state)
            child_node = TreeNode(child_state, cost=child_cost, heuristic=child_heuristic, parent=current_node)
            frontier.put(child_node)

    return None


