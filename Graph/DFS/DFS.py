# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict  # if a key that is not in the dict is attempt


# This class represents a directed graph
# adjacency list representation - a dictionary of sets
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        # self.graph = defaultdict(list)
        self.graph = defaultdict(set)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].add(v)


    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print( v,)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)

    # Driver code


# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

# This code is contributed by Neelam Yadav