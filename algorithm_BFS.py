from collections import deque
from utils_algorithms import TreeNode, get_child_states
from objective_test import objective_test

def breadth_first_search(level):
    root = TreeNode(level.atoms_list)   # create the root node in the search tree
    queue = deque([root])   # initialize the queue to store the nodes

    visited_states = []
    visited_states.append(root.state)
    
    while queue:
        node = queue.popleft()   # get first element in the queue
        if objective_test(level.matrix, node.state, level.molecule):   # check goal state
            return node
        
        for state in get_child_states(level.matrix, node.state):   # go through next states
            if state not in visited_states:
                # create tree node with the new state
                child = TreeNode(state, node)
                
                # link child node to its parent in the tree
                node.add_child(child)
                visited_states.append(child.state)
                # enqueue the child node
                queue.append(child)
        
    return None
