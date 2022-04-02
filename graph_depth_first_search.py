# Implementing a Graph - Depth First Search (DFS)
# Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
# The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and 
# explores as far as possible along each branch before backtracking.

# Assignment
# Complete the depth_first_search and depth_first_search_r methods. The depth_first_search_r is the recursive 
# helper method for depth_first_search.

# depth_first_search()
# depth_first_search takes a start vertex as input. It will traverse the graph in a depth-first manner and record the 
# vertices it visits to a list. That list will be returned.
# It should:
# Create an empty visited list.
# Call depth_first_search_r with the the empty list and the start vertex
# Return the visited array after depth_first_search_r has mutated it

# depth_first_search_r()
# depth_first_search_r takes a list of vertices that have been visited so far and a current vertex as input.
# It should:
# Visit the current vertex by adding it to the visited list
# For each connected vertex to the current vertex:
# If the neighboring vertex hasn't been visited yet, visit it by recursively calling depth_first_search_r with the neighboring vertex

class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        for neighbor in self.graph[current_vertex]:
            if neighbor not in visited:
                self.depth_first_search_r(visited,neighbor)
        


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
    graph.add_edge(1, 5)
    graph.add_edge(1, 3)
    graph.add_edge(2, 6)
    graph.add_edge(5, 4)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    print(graph)
    print(graph.depth_first_search(1))


main()
