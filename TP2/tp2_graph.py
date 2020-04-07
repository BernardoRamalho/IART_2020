from collections import defaultdict


class Graph:

    def __init__(self, operators, validation_functions, initial_state):
        self.start_state = initial_state
        self.operators = operators
        self.validation_functions = validation_functions
        self.graph = defaultdict(list)
        self.reverse_graph = defaultdict(list)

    def add_edge(self, father_node, children):
        self.graph[father_node].append(children)

    def print_solution(self, node):
        solution = []
        while node in list(self.reverse_graph.keys()):
            solution.insert(0, node)
            node = self.reverse_graph[node][0]

        solution.insert(0, self.start_state)

        for i in solution:
            print(i)

    def __run_graph(self, s, function):

        # Mark all the vertices as not visited
        visited = defaultdict(bool)

        # Create a queue for BFS
        queue = [s]

        # Mark the source node as visited and enqueu it
        visited[s] = True
        finished = True

        n = 0
        while finished:

            # Dequeu a vertex from queue and print it
            s = queue.pop(0)
            for i in self.operators(s):
                self.add_edge(s, i)

                if i not in visited:
                    self.reverse_graph[i]. append(s)

            for i in self.graph[s]:

                if self.validation_functions(s):
                    print("HEy")
                    finished = False
                    self.print_solution(s)
                    print(n)
                    break
                elif not visited[i]:
                    function(i, queue, visited, n)

            n += 1


    @staticmethod
    def __bfs(i, queue, visited, _):
        queue.append(i)
        visited[i] = True

    @staticmethod
    def __dfs(i, queue, visited, _):
        queue.insert(0, i)
        visited[i] = True

    @staticmethod
    def __iterative(i, queue, visited, n):
        if n % 2 != 0:
            queue.append(i)
        else:
            queue.insert(0, i)
        visited[i] = True
        return True

    def bfs(self):
        self.__run_graph(self.start_state, self.__bfs)

    def dfs(self):
        self.__run_graph(self.start_state, self.__dfs)

    def iterative_dfs(self):
        self.__run_graph(self.start_state, self.__iterative)

    def ask_mode(self):
        mode = input("Which mode do you wish?\n1.bfs\n2.dfs\n3.iterative\nInsert the chosen name mode: ")

        if mode != 'bfs' and mode != 'dfs' and mode != 'iterative':
            return self.ask_mode_again()
        else:
            return mode

    def ask_mode_again(self):
        mode = input("Insert a valid name mode(bfs or dfs or iterative): ")

        if mode != 'bfs' and mode != 'dfs' and mode != 'iterative':
            return self.ask_mode_again()
        else:
            return mode
