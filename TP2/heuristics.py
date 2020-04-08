def count_displaced_pieces(state, end_state):
    nr_displaced_pieces = 0

    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] != end_state[i][j]:
                nr_displaced_pieces += 1

    return nr_displaced_pieces


def calculate_manhattan_distance(state, end_state):
    manhattan_distance = 0

    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] != end_state[i][j] and state[i][j] != 0:
                correct_x = (state[i][j] - 1) % 3
                correct_y = (state[i][j] - 1) // 3
                manhattan_distance += abs(correct_x - j) + abs(correct_y - i)

    return manhattan_distance


def value_node(node, end_state):
    if node.state == end_state:
        node.value = -1
    node.value = count_displaced_pieces(node.state, end_state) + calculate_manhattan_distance(node.state,
                                                                                              end_state) + node.cost
