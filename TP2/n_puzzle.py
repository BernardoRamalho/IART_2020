import random
import math
import copy
import time
from uninformed_search import Graph
import informed_search


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

    for i in range(1, len(board) * len(board)):

        if board[height][width] != i:
            return False

        width += 1

        if width % 3 == 0:
            width = 0
            height += 1

    return True


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


def question_2_1_b():
    start_time = time.time()

    board = ((1, 6, 2),
             (5, 7, 3),
             (0, 4, 8))

    graph = Graph(operators, validate_n_puzzle, board)
    graph.bfs()

    print("It took", time.time() - start_time, "seconds to complete the computation of question 2.1.b.")


def question_2_1_c():
    start_time = time.time()

    end_board = ((1, 2, 3),
                 (4, 5, 6),
                 (7, 8, 0))

    board = ((1, 6, 2),
             (5, 7, 3),
             (0, 4, 8))

    print(board)

    informed_search.astar(board, end_board, operators)

    print("It took", time.time() - start_time, "seconds to complete the computation of question 2.1.c.")


def question_2_1_d_astar():
    end_board_9 = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 0))

    end_board_16 = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 16))

    # Resolve First Board
    start_time = time.time()
    prob1 = ((1, 2, 3),
             (5, 0, 6),
             (4, 7, 8))
    informed_search.astar(prob1, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob1.")

    # Resolve Second Board
    start_time = time.time()
    prob2 = ((1, 3, 6),
             (5, 2, 0),
             (4, 7, 8))
    informed_search.astar(prob2, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob2.")

    start_time = time.time()
    prob3 = ((1, 6, 2),
             (5, 7, 3),
             (0, 4, 8))
    informed_search.astar(prob3, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob3.")

    start_time = time.time()
    prob4 = ((5, 1, 3, 4),
             (2, 0, 7, 8),
             (10, 6, 11, 12),
             (9, 13, 14, 15))
    informed_search.astar(prob4, end_board_16, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob4.")

def question_2_1_d_greedy():
    end_board_9 = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 0))

    end_board_16 = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 16))

    # Resolve First Board
    start_time = time.time()
    prob1 = ((1, 2, 3),
             (5, 0, 6),
             (4, 7, 8))
    informed_search.greedy(prob1, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob1.")

    # Resolve Second Board
    start_time = time.time()
    prob2 = ((1, 3, 6),
             (5, 2, 0),
             (4, 7, 8))
    informed_search.greedy(prob2, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob2.")

    start_time = time.time()
    prob3 = ((1, 6, 2),
             (5, 7, 3),
             (0, 4, 8))
    informed_search.greedy(prob3, end_board_9, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob3.")

    start_time = time.time()
    prob4 = ((5, 1, 3, 4),
             (2, 0, 7, 8),
             (10, 6, 11, 12),
             (9, 13, 14, 15))
    informed_search.greedy(prob4, end_board_16, operators)
    print("It took", time.time() - start_time, "seconds to complete the computation of Prob4.")


def main():
    # Exercises
    #question_2_1_b()
    #question_2_1_c()
    #question_2_1_d_astar()
    question_2_1_d_greedy()


if __name__ == "__main__":
    main()
