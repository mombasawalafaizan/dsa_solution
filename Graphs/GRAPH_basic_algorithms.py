from collections import defaultdict
from queue import Queue


class Heap:
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = dict()

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:

            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    # Standard function to extract minimum
    # node from heap
    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:

            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            # move to parent index
            i = (i - 1) // 2

    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


class GraphNode:
    def __init__(self, data, w=0):
        self.data = data
        self.w = w

    def __str__(self):
        s = "Data: " + str(self.data) + " "
        return s if self.w == 0 else s + "Weight: " + str(self.w) + " "


class Graph:
    def __init__(self, V, bidirectional=True, weighted=False):
        self.graph = defaultdict(list)
        self.V = V
        self.bidirectional = bidirectional
        self.weighted = weighted

    def addEdge(self, u, v, w=0):
        self.graph[u].append(GraphNode(v, w))
        if self.bidirectional:
            self.graph[v].append(GraphNode(u, w))

    # Graph Algorithms

    # BFS
    def BFS(self, s):
        vis = dict()
        q = Queue()
        q.put(s)
        for node in self.graph:
            vis[node] = False
        vis[s] = True
        print("BFS traversal:", end=" ")
        while not q.empty():
            cur_node = q.get()
            print(cur_node, end=" ")
            for adj in self.graph[cur_node]:
                if not vis[adj.data]:
                    vis[adj.data] = True
                    q.put(adj.data)
        print()

    # DFS
    def DFS(self, s):
        vis = dict()
        for node in self.graph:
            vis[node] = False
        print("DFS traversal:", end=" ")
        self._dfs_helper(s, vis)
        print()

    def _dfs_helper(self, u, vis):
        vis[u] = True
        print(u, end=" ")
        for adj in self.graph[u]:
            if not vis[adj.data]:
                self._dfs_helper(adj.data, vis)

    # BFS single source shortest path
    # NOTE
    # 1): Use BFS SSSP in case of NON-WEIGHTED GRAPHS
    #     This will find the distance in terms of least number of edges between two nodes
    # 2): If we have to find the distance between source to a particular destination,
    #     optimize the BFS search by breaking the loop once the destination is reached
    #     Same do for Dijkstra also

    def getShortestPaths(self, source, dest="!"):
        parent = dict()
        distance = {u: float("inf") for u in self.graph}
        self._bfs_sssp(source, parent, distance, dest)
        # Print shortest path for each node
        if dest == "!":
            for u in self.graph:
                print(
                    "Distance from " + source + " to " + u + " is " + str(distance[u])
                )
        else:
            print(
                "Distance from " + source + " to " + dest + " is " + str(distance[dest])
            )
            print("Shortest Path: ", end=" ")
            temp = dest
            while parent[temp] != temp:
                print(temp, "<--", end=" ")
                temp = parent[temp]
            print(source)

    def _bfs_sssp(self, source, parent, distance, dest):
        q = Queue()
        q.put(source)
        distance[source] = 0
        parent[source] = source
        while not q.empty():
            cur_node = q.get()
            for adj in self.graph[cur_node]:
                if distance[adj.data] == float("inf"):
                    q.put(adj.data)
                    distance[adj.data] = distance[cur_node] + 1
                    parent[adj.data] = cur_node
                if dest == adj.data:
                    break

    # The main function that calulates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src):

        V = self.V  # Get the number of vertices in graph
        dist = dict()  # dist values used to pick minimum
        # weight edge in cut
        parent = {src: src}
        # minHeap represents set E
        minHeap = Heap()

        # Initialize min heap with all vertices.
        # dist value of all vertices
        i = 0
        src_pos = -1
        for v in self.graph:
            if v == src:
                src_pos = i
            dist[v] = float("inf")
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos[v] = i
            i += 1

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src_pos
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl.data

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (
                    minHeap.isInMinHeap(v)
                    and dist[u] != float("inf")
                    and (pCrawl.w + dist[u]) < dist[v]
                ):
                    dist[v] = pCrawl.w + dist[u]

                    # update distance value
                    # in min heap also
                    minHeap.decreaseKey(v, dist[v])
                    parent[v] = u

        return dist, parent

    # Prim's algorithm
    def primsMST(self):
        # Pick any node
        src = next(iter(self.graph.keys()))
        V = self.V  # Get the number of vertices in graph
        key = dict()  # dist values used to pick minimum
        # weight edge in cut
        parent = {src: -1}
        # minHeap represents set E
        minHeap = Heap()

        # Initialize min heap with all vertices.
        # dist value of all vertices
        i = 0
        src_pos = -1
        for v in self.graph:
            if v == src:
                src_pos = i
            key[v] = float("inf")
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos[v] = i
            i += 1

        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src_pos
        key[src] = 0
        minHeap.decreaseKey(src, dist[src])

        # Initially size of min heap is equal to V
        minHeap.size = V

        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:

            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl.data

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl.w < key[v]:
                    key[v] = pCrawl.w
                    parent[v] = u

                    # update distance value
                    # in min heap also
                    minHeap.decreaseKey(v, key[v])

        self.printArr(parent, V)

    def printArr(self, parent, n):
        for i in parent:
            print(str(parent[i]) + " - " + str(i))

    # Kruskal's algorithm
    def find(self, parent, i):
        """A utility function to find set of an element i"""
        # Parent node will have negative values, else
        if type(parent[i]) is not str and parent[i] < 0:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Check if xroot or yroot has more childs and make the suitable parent
        if parent[xroot] <= parent[yroot]:
            parent[xroot] = parent[xroot] + parent[yroot]
            parent[yroot] = xroot
        else:
            parent[yroot] = parent[xroot] + parent[yroot]
            parent[xroot] = yroot

    def kruskalMST(self):
        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing
        # order of their weight.
        # Do BFS search to build this kind of graph
        # eg. [u, v, w]
        edges = []
        vis = {u: False for u in self.graph}
        for u in self.graph:
            for adj in self.graph[u]:
                if vis[adj.data] == False:
                    edges.append([u, adj.data, adj.w])
            vis[u] = True
        edges.sort(key=lambda x: x[2])

        parent = {}

        # Create V subsets with single elements
        for node in self.graph:
            parent[node] = -1

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, x, y)
            # Else discard the edge

        # print the contents of result[] to display the built MST
        min_weights = 0
        print("Following are the edges in the constructed MST:")
        for u, v, weight in result:
            print("%s -- %s == %d" % (u, v, weight))
            min_weights += weight
        print("\nTotal weight of MST: ", min_weights)


if __name__ == "__main__":
    g = Graph(9, True, True)
    g.addEdge("0", "1", 4)
    g.addEdge("0", "7", 8)
    g.addEdge("1", "7", 11)
    g.addEdge("1", "2", 8)
    g.addEdge("7", "8", 7)
    g.addEdge("2", "8", 2)
    g.addEdge("8", "6", 6)
    g.addEdge("2", "5", 4)
    g.addEdge("6", "5", 2)
    g.addEdge("2", "3", 7)
    g.addEdge("3", "3", 14)
    g.addEdge("3", "4", 9)
    g.addEdge("5", "4", 10)
    g.addEdge("7", "6", 1)
    g.BFS("0")
    g.DFS("0")
    print(
        "\n---------------------BFS single source shortest path---------------------------"
    )
    g.getShortestPaths("0", "5")
    print("\n---------------------DIJKSTRA---------------------------")
    dist, parent = g.dijkstra("0")
    print("Distance from 0 for node 5: ", dist["5"])
    print("Path to 5: ", end=" ")
    temp = "5"
    while parent[temp] != temp:
        print(temp, "<--", end=" ")
        temp = parent[temp]
    print("0")
    print("----------------------------Prim's MST----------------------------")
    g.primsMST()
    print("----------------------------Kruskal's MST----------------------------")
    g.kruskalMST()
