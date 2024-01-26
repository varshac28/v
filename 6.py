class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        # Simple heuristic function (constant 1)
        return 1

    def a_star_algorithm(self, start_node, stop_node):
        open_list = {start_node}
        closed_list = set()

        g = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            n = min(open_list, key=lambda node: g[node] + self.h(node))

            if n == stop_node:
                path = [n]
                while n != start_node:
                    n = parents[n]
                    path.append(n)
                path.reverse()
                return path

            open_list.remove(n)
            closed_list.add(n)

            for m, weight in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

        return None
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1 = Graph(adjacency_list)
result = graph1.a_star_algorithm('A', 'D')
print("Path:", result)
