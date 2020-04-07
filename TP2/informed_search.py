from collections import defaultdict
import heuristics


class Node:

    def __init__(self, parent, state, value, cost=0):
        self.parent = parent
        self.state = state
        self.cost = cost  # For A* it will be changed to 1 since Greedy doesnt care about cost
        self.value = value

    def __eq__(self, other):
        return self.state == other.state


def generate_children(father_node, operations, heuristic_func_number, end_state, open_list):
    for i in operations(father_node.state):
        child = Node(father_node, i, 0, 1)
        heuristics.value_node(heuristic_func_number, child, end_state)
        open_list[child.value] = child


def get_minimum_value_index(open_list):
    min_value = 10000
    best_index = 0
    for i in range(len(open_list)):
        if open_list[i].value < min_value:
            min_value = open_list[i].value
            best_index = i

    return best_index


def print_solution_path(node):
    path = []

    while node.parent is not None:
        path.insert(0, node.state)
        node = node.parent

    print("Path to solution:")
    for i in path:
        print(i)


def astar(start_state, end_state, operations, heuristic_func_number):
    closed_list = []
    open_list = []

    beggining_node = Node(None, start_state, 0)
    ending_node = Node(None, end_state, 0)

    open_list.append(beggining_node)

    while len(open_list) > 0:

        current_index = get_minimum_value_index(open_list)

        # Popping the best node from the open_list and putting on the closed list (so it won't be seen again)
        current_node = open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == ending_node:
            print_solution_path(current_node)
            break

        # Generate the children
        for i in operations(current_node.state):
            child = Node(current_node, i, 0, current_node.cost + 1)
            heuristics.value_node(heuristic_func_number, child, end_state)
            not_worth = False

            for closed_child in closed_list:
                if closed_child == child:
                    continue

            for open_child in open_list:
                if open_child == child and open_child.cost > child.cost:
                    open_child.parent = child.parent
                    open_child.cost = child.cost
                    heuristics.value_node(heuristic_func_number, open_child, end_state)
                    break

            if child == ending_node:
                open_list.append(child)
                break
            else:
                open_list.append(child)
