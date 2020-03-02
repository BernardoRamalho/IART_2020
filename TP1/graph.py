from collections import defaultdict


class Graph:

    def __init__(self, limit, operators, validation_functions):
        self.limit = limit
        self.operators = operators
        self.validation_functions = validation_functions
        self.graph = defaultdict(list)

    def add_edge(self, father_node, children):
        self.graph[father_node].append(children)

    def __run_graph(self, s, function):

        # Mark all the vertices as not visited
        visited = defaultdict(bool)

        # Create a queue for BFS
        queue = [s]

        # Mark the source node as visited and enqueu it
        visited[s] = True
        finished = True
        n = 0
        while finished and n < self.limit:

            # Dequeu a vertex from queue and print it
            s = queue.pop(0)
            print(s)
            for i in self.operators(s):
                self.add_edge(s, i)

            for i in self.graph[s]:

                if self.validation_functions(s):
                    finished = False
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

    def __iterative(self, i, queue, visited, n):
        if n % self.limit == 0:
            queue.append(i)
        else:
            queue.insert(0, i)
        visited[i] = True
        return True

    def bfs(self, s):
        self.__run_graph(s, self.__bfs)

    def dfs(self, s):
        self.__run_graph(s, self.__dfs)

    def iterative_dfs(self, s):
        self.__run_graph(s, self.__iterative)
