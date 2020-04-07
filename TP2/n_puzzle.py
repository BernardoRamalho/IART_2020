import random
import math
import copy
import time
from tp2_graph import Graph


##############################
#                            #
# N PUZZLE RELATED FUNCTIONS #
#                            #
##############################


def get_zero_position(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j


def validate_n_puzzle(board):
    width = 0
    height = 0

    for i in range(1, len(board)*len(board)):

        if board[height][width] != i:
            return False

        width += 1

        if width % 3 == 0:
            width = 0
            height += 1



    return True


def create_board(size):
    random.seed()  # Initiate Random Generator
    numbers_used = []  # List to keep track of numbers already used
    board = [[]]  # Initial Board
    width = 0
    for i in range(size):
        number = random.randint(0, size - 1)  # Generate Random Number

        while number in numbers_used:  # If number already exists generate another until a new
            number = random.randint(0, size - 1)  # is found

        numbers_used.append(number)  # Add the new number to the list of used ones

        board[width].append(number)

        if (i + 1) % math.sqrt(size) == 0 and i + 1 < size:  # Checks if we reached the end of a line
            board.append([])  # Create a new Line
            width += 1

    return list_of_list_to_tuple_of_tuples(board)


def print_puzzle(board):
    for i in board:
        print(i)


##############################
#                            #
# MOVEMENT RELATED FUNCTIONS #
#                            #
##############################

# To note: the direction of the movement is related to where the 0 moves


def move_right(zero_position, board):
    new_y = zero_position[1] + 1

    board[zero_position[0]][zero_position[1]] = board[zero_position[0]][new_y]
    board[zero_position[0]][new_y] = 0

    return list_of_list_to_tuple_of_tuples(board)


def move_left(zero_position, board):
    new_y = zero_position[1] - 1

    board[zero_position[0]][zero_position[1]] = board[zero_position[0]][new_y]
    board[zero_position[0]][new_y] = 0

    return list_of_list_to_tuple_of_tuples(board)


def move_down(zero_position, board):
    new_x = zero_position[0] + 1

    board[zero_position[0]][zero_position[1]] = board[new_x][zero_position[1]]
    board[new_x][zero_position[1]] = 0

    return list_of_list_to_tuple_of_tuples(board)


def move_up(zero_position, board):
    new_x = zero_position[0] - 1

    board[zero_position[0]][zero_position[1]] = board[new_x][zero_position[1]]
    board[new_x][zero_position[1]] = 0

    return list_of_list_to_tuple_of_tuples(board)


def operators(board):
    zero_position = get_zero_position(board)
    board_list = tuple_of_tuples_to_list_of_lists(board)

    board_states = []

    if zero_position[1] + 1 <= len(board) - 1:
        board_states.append(move_right(zero_position, copy.deepcopy(board_list)))

    if zero_position[1] - 1 >= 0:
        board_states.append(move_left(zero_position, copy.deepcopy(board_list)))

    if zero_position[0] + 1 <= len(board) - 1:
        board_states.append(move_down(zero_position, copy.deepcopy(board_list)))

    if zero_position[0] - 1 >= 0:
        board_states.append(move_up(zero_position, copy.deepcopy(board_list)))

    return board_states


############################
#                          #
# SEARCH RELATED FUNCTIONS #
#                          #
############################

def list_of_list_to_tuple_of_tuples(list_of_lists):
    list_of_tuples = []
    for i in list_of_lists:
        list_of_tuples.append(tuple(i))
    return tuple(list_of_tuples)


def tuple_of_tuples_to_list_of_lists(tuple_of_tuples):
    list_of_lists = []
    for i in tuple_of_tuples:
        list_of_lists.append(list(i))
    return list_of_lists


options = {
    "dfs": lambda graph: graph.dfs(),
    "iterative": lambda graph: graph.iterative_dfs(),
    "bfs": lambda graph: graph.bfs()
}


def main():
    start_time = time.time()
    # Initialize the puzzle
    puzzle_size = int(input("Introduce a size (must be perfect squares like 9 and 16): "))
    puzzle = create_board(puzzle_size)
    puzzles = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

    # Initialize the graph
    graph = Graph(operators, validate_n_puzzle, puzzle)

    # Run the Search
    mode = graph.ask_mode()
    options[mode](graph)
    print("It took", time.time() - start_time, "seconds to complete the computation.")


if __name__ == "__main__":
    main()
