from collections import deque
from operators import *
import numpy as np

class TreeNode:
    def __init__(self, state, cost=0, heuristic=0, parent=None):
        self.state = state.copy()
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
        self.children = []
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic
        


def get_child_states(level_matrix, state):
    new_states = []

    for i in range(0, len(state)):
        new_states.append(move_left(level_matrix, i, state))
        new_states.append(move_up(level_matrix, i, state))
        new_states.append(move_right(level_matrix, i, state))
        new_states.append(move_down(level_matrix, i, state))
    
    return new_states



def print_solution(node):
    solution = deque([node])
    
    while node.depth != 0:
        solution.appendleft(node.parent)
        node = node.parent

    for i in solution:
        print(i.state)
        #print(i.cost)

    return
