from TP1.tp1_graph import Graph
import time

def validate_function(banks):
    return banks[1][0] == 3 and banks[1][1] == 3 and banks[0][0] == 0 and banks[0][1] == 0


def check_more_missionaries(bank):

    if bank[0] == 0 and bank[1] > 0:
        return True

    return bank[0] >= bank[1]


"""


Operators Functions


"""


def send_2_missionaries(initial_bank, final_bank, resulting_state):
    if initial_bank[0] < 2:
        return

    initial_bank[0] -= 2
    final_bank[0] += 2

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), True)

        resulting_state.append(state)


def send_missionary_cannibal(initial_bank, final_bank, resulting_state):
    if initial_bank[1] == 0 or initial_bank[0] == 0:
        return

    initial_bank[0] -= 1
    initial_bank[1] -= 1

    final_bank[0] += 1
    final_bank[1] += 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), True)

        resulting_state.append(state)


def send_2_cannibals(initial_bank, final_bank, resulting_state):
    if initial_bank[1] < 2:
        return

    initial_bank[1] -= 2

    final_bank[1] += 2

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), True)

        resulting_state.append(state)


def send_missionary(initial_bank, final_bank, resulting_state):
    if initial_bank[0] == 0:
        return

    initial_bank[0] -= 1

    final_bank[0] += 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), True)

        resulting_state.append(state)


def send_cannibal(initial_bank, final_bank, resulting_state):
    if initial_bank[1] == 0:
        return

    initial_bank[1] -= 1

    final_bank[1] += 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), True)

        resulting_state.append(state)


def send_back_2_missionaries(initial_bank, final_bank, resulting_state):
    if final_bank[0] < 2:
        return

    initial_bank[0] += 2

    final_bank[0] -= 2

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), False)

        resulting_state.append(state)


def send_back_missionary_cannibal(initial_bank, final_bank, resulting_state):
    if final_bank[1] == 0 or final_bank[0] == 0:
        return

    initial_bank[0] += 1
    initial_bank[1] += 1

    final_bank[0] -= 1
    final_bank[1] -= 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), False)

        resulting_state.append(state)


def send_back_2_cannibals(initial_bank, final_bank, resulting_state):
    if final_bank[1] < 2:
        return

    initial_bank[1] += 2

    final_bank[1] -= 2

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), False)

        resulting_state.append(state)


def send_back_missionary(initial_bank, final_bank, resulting_state):
    if final_bank[0] == 0:
        return

    initial_bank[0] += 1

    final_bank[0] -= 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), False)

        resulting_state.append(state)


def send_back_cannibal(initial_bank, final_bank, resulting_state):
    if final_bank[1] == 0:
        return

    initial_bank[1] += 1

    final_bank[1] -= 1

    if check_more_missionaries(initial_bank) and check_more_missionaries(final_bank):
        state = (tuple(initial_bank), tuple(final_bank), False)

        resulting_state.append(state)


"""
banks is a tuple with the following format:
    -banks[0] corresponds to the initial bank of the river
    -banks[1] corresponds to the final bank of the river
    -banks[2] corresponds to a boolean to indicate where the boat is (True if the boat is on the final bank)
"""


def operators(banks):
    initial_bank = [banks[0][0], banks[0][1]]
    final_bank = [banks[1][0], banks[1][1]]

    resulting_states = []

    if not banks[2]:
        send_2_cannibals(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_2_missionaries(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_cannibal(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_missionary(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_missionary_cannibal(initial_bank.copy(), final_bank.copy(), resulting_states)

    if banks[2]:
        send_back_2_cannibals(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_back_2_missionaries(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_back_cannibal(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_back_missionary(initial_bank.copy(), final_bank.copy(), resulting_states)
        send_back_missionary_cannibal(initial_bank.copy(), final_bank.copy(), resulting_states)

    return resulting_states


banks = ((3, 3), (0, 0), False)

options = {
    "dfs": lambda graph: graph.dfs(),
    "iterative": lambda graph: graph.iterative_dfs(),
    "bfs": lambda graph: graph.bfs()
}
def main():
    start_time = time.time()
    graph = Graph(operators, validate_function, banks)
    mode = graph.ask_mode()
    options[mode](graph)
    print("It took", time.time() - start_time, "seconds to complete the computation.")

if __name__ == "__main__":
    main()