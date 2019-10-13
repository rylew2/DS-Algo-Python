# Algorithm:
# Steps involved in finding the topological ordering of a DAG:
#
# 1) Compute in-degree (number of incoming edges) for each of the vertex present in the DAG and initialize the count of visited nodes as 0.
#
# 2) Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
#
# 3) Remove a vertex from the queue (Dequeue operation) and then.
#
# Increment count of visited nodes by 1.
# Decrease in-degree by 1 for all its neighboring nodes.
# If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
# Step 5: Repeat Step 3 until the queue is empty.
#
# Step 5: If count of visited nodes is not equal to the number of nodes in the graph then the topological sort is not possible for the given graph.


# A Python program to print topological sorting of a graph
# using indegrees
from collections import defaultdict, deque


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(set)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def addVertex(self, u):
        self.graph[u]
        # The function to do Topological Sort.


    # O(V+E) / O(V+E)
    def bfs_topological_sort(self):
        in_degree = defaultdict(int)
        for i in self.graph:   # traverse graph and intialize in_degree O(V+E) time
            for j in self.graph[i]:
                if not in_degree[j]: in_degree[j]
                in_degree[j] += 1

        queue = deque([])
        for i in range(self.V): # O(V)
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        top_order = [] # topological ordering

        while queue:  # One by one dequeue vertices from queue and enqueue adjacents if indegree of adjacent becomes 0

            u = queue.popleft() # extract from front of q and add to topological roder
            top_order.append(u)

            for i in self.graph[u]: # Iterate through all neighbouring nodes of dequeued node u and decrease their in-degree by 1
                in_degree[i] -= 1
                if in_degree[i] == 0: # If in-degree becomes zero, add it to queue
                    queue.append(i)
            cnt += 1

        # Check if there was a cycle
        if cnt != len(self.graph):
            print("There exists a cycle in the graph")
        else:
            # Print topological order
            print(top_order)


    # simply get toposort  (doesn't detect cycle)
    # O(V+E) / O(V)
    def dfs_topological_sort(self):
        def tsutil(v, deq, visited):
            visited.add(v)
            for i in self.graph[v]:
                if i not in visited:
                    tsutil(i, deq, visited)
            deq.appendleft(v)

        deq, visited = deque(), set()
        for i in self.graph:
            if i not in visited:
                tsutil(i, deq, visited)

        print(deq)




g = Graph(6)
for i in range(6): g.addVertex(i)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
# g.addEdge(1,4)
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.bfs_topological_sort()
g.dfs_topological_sort()