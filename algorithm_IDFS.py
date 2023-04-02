from utils_algorithms import TreeNode, get_child_states
from objective_test import objective_test

def iterative_deepening_search(level, depth):
    root = TreeNode(level.atoms_list)
    while True:
        result = depth_limited_search(level, root, depth)
        if result != 'cutoff':
            return result
        depth += depth

def depth_limited_search(level, node, depth, visited=None):
    if visited is None:
        visited = [node.state]
        #visited_states = []
    if objective_test(level.matrix, node.state, level.molecule):
        return node
    elif depth == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        
        for state in get_child_states(level.matrix, node.state):
            if state not in visited:
                print(state)
                visited.append(state)
                child = TreeNode(state, parent=node)
                node.add_child(child)
                result = depth_limited_search(level, child, depth-1, visited)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
        #visited.remove(node.state)
        return 'cutoff' if cutoff_occurred else None



'''''
def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        result = depth_limited_search(graph, start, goal, depth)
        if result != 'cutoff':
            return result
        depth += 1

def depth_limited_search(graph, node, goal, depth, visited=None):
    if visited is None:
        visited = set()
    if node == goal:
        return [node]
    elif depth == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = depth_limited_search(graph, neighbor, goal, depth-1, visited)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return [node] + result
        visited.remove(node)
        return 'cutoff' if cutoff_occurred else None
        '''