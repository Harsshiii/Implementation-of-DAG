from collections import defaultdict

class DAG:
    def __init__(self, vertices):
        """
        Initialize the graph with given number of vertices
        """
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add a directed edge from u to v
        """
        self.graph[u].append(v)

    def _is_cyclic_util(self, v, visited, rec_stack):
        """
        Utility function for cycle detection using DFS
        """
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self._is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        """
        Check if the graph contains a cycle
        """
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:
                if self._is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

    def _topological_sort_util(self, v, visited, stack):
        """
        Utility function for topological sort
        """
        visited[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self._topological_sort_util(neighbour, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        """
        Perform topological sorting
        """
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self._topological_sort_util(i, visited, stack)

        return stack


if __name__ == "__main__":
    # Example usage
    g = DAG(6)

    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    if g.is_cyclic():
        print("Graph is NOT a DAG")
    else:
        print("Graph is a DAG")
        print("Topological Sort:", g.topological_sort())