# Implementing a Graph - Breadth First Search (BFS)
# Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root 
# (or some arbitrary node of a graph), and explores all of the neighbour nodes at the present depth prior to moving on to the 
# nodes at the next depth level.

# Assignment
# Complete the breadth_first_search method.
# breadth_first_search()
# breadth_first_search takes a start vertex as input. It will traverse the graph in a breadth-first manner and record the 
# vertices it visits to a list. That list will be returned.

# It should:
# Create an empty visited list.
# Create an empty to_visit list.
# Queue up the start vertex by adding it the the to_visit list.
# While to_visit is not empty:
# Pop the first vertex off the to_visit list and visit it by appending it to visited
# For each neighbor of the vertex we just visited:
# If the neighbor hasn't been visited:
# Queue up the neighbor by adding it to the to_visit loop
# Once to_visit is empty, we've traversed the whole graph so just return visited

class Graph:
    def breadth_first_search(self, v):
        visited = []
        q = [v] #queue
        while len(q) > 0:
            current = q.pop()
            visited.append(current)
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    q.insert(0,neighbor)
        return visited


        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        return str(self.graph)


def main():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(4, 8)
    graph.add_edge(6, 9)
    print(graph)
    print(graph.breadth_first_search(1))


main()
