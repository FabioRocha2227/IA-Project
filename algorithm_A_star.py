from utils_algorithms import TreeNode, get_child_states
from evaluation_function import evaluate_distances, evaluate_links_and_distances
from objective_test import objective_test, evaluate_missing_links
from queue import PriorityQueue

#heuristic=evaluate_distances(level.atoms_list)

def a_star(level):
    frontier = PriorityQueue()
    root = TreeNode(level.atoms_list, cost=0, heuristic=evaluate_links_and_distances(level.matrix, level.atoms_list, level.molecule))
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
            child_heuristic = evaluate_links_and_distances(level.matrix, child_state, level.molecule)
            child_node = TreeNode(child_state, cost=child_cost, heuristic=child_heuristic, parent=current_node)
            frontier.put(child_node)

    return None



'''
from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

def astar_tree(start, goal, h):
    frontier = PriorityQueue()
    start_node = Node(start, cost=0, heuristic=h(start, goal))
    frontier.put(start_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        if current_state == goal:
            return current_node

        explored.add(current_state)

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state in explored:
                continue

            neighbor_cost = current_node.cost + 1  # assuming edge cost of 1
            neighbor_heuristic = h(neighbor_state, goal)
            neighbor_node = Node(neighbor_state, parent=current_node, cost=neighbor_cost, heuristic=neighbor_heuristic)
            frontier.put(neighbor_node)

    return None
    '''