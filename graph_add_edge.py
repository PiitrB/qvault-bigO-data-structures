# Assignment
# Complete the constructor and the add_edge methods.

# Constructor
# The constructor should create an empty dictionary as a data member called graph.
# add_edge(self, u, v)
# add_edge takes two vertices as inputs, and should add an edge to the adjacency list (the dictionary).
# The dictionary maps vertices to a set of all other vertices they share an edge with. For example:
# {
#     "0": [1, 4],
#     "1": [0, 2, 3, 4],
#     "2": [1, 3],
#     "3": [1, 2, 4],
#     "4": [0, 1, 3]
# }
# This is accomlished using the following steps:
# If vertex u is already a key in the dictionary, add v to u's set. Otherwise, create a new set for u that contains v.
# Repeat the same steps, but swap u and v.
# Set operations
# Sets are like Lists, but they are unordered and they guarantee uniqueness. There can be no two of the same value in a set.
# A set can be created from a normal List in the following way:
# s = set([1, 2, 3, 3, 4, 4])
# # results in s = [1, 2, 3, 4]
# You can add to an existing set the following way:

# s = set([1])
# s.add(2)
# # results in s = [1, 2]

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            if isinstance(self.graph[u], set):
                self.graph[u].add(v)
            else:
                temp_set = set([self.graph[u]])
                temp_set.add(v)
                self.graph[u] = temp_set
        else:
            self.graph[u] = v

        if v in self.graph:
            if isinstance(self.graph[v], set):
                self.graph[v].add(u)
            else:
                temp_set = set([self.graph[v]])
                temp_set.add(u)
                self.graph[v] = temp_set
        else:
            self.graph[v] = u


# qvault's solution: much more elegant  :)
# def add_edge(self, u, v):
#         if u in self.graph.keys():
#             self.graph[u].add(v)
#         else:
#             self.graph[u] = set([v])
#         if v in self.graph.keys():
#             self.graph[v].add(u)
#         else:
#             self.graph[v] = set([u])
        
        

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def __repr__(self):
        return str(self.graph)


def main():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(4, 3)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    print(graph)


main()
