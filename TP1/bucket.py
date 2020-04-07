from TP1.tp1_graph import Graph
import time


def validate_buckets(buckets_state):
    return buckets_state[0] == 2


def get_all_operators(buckets_state):
    b1 = buckets_state[0]
    b2 = buckets_state[1]
    states = []

    if b1 < 4:
        states.append((4, b2))
    if b2 < 3:
        states.append((b1, 3))
    if b1 > 0:
        states.append((0, b2))
    if b2 > 0:
        states.append((b1, 0))
    if b1 + b2 >= 3 and b2 < 3:
        states.append((b1 - (3 - b2), 3))
    if b1 + b2 < 3 and b1 < 0:
        states.append((0, b2 + b1))
    if b1 + b2 >= 4 and b1 < 4:
        states.append((4, b2 - (3 - b1)))
    if b1 + b2 < 4 and b2 < 0:
        states.append((b2 + b1, 0))

    return states


options = {
    "dfs": lambda graph: graph.dfs(),
    "iterative": lambda graph: graph.iterative_dfs(),
    "bfs": lambda graph: graph.bfs()
}


def main():
    start_time = time.time()
    graph = Graph(get_all_operators, validate_buckets, (0, 0))
    mode = graph.ask_mode()
    options[mode](graph)
    print("It took", time.time() - start_time, "seconds to complete the computation.")


if __name__ == "__main__":
    main()
