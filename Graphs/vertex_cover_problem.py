# This is a NP-hard problem

# Approximate solution
# Algorithm:
# 1) Initialize the result as {}
# 2) Consider a set of all edges in given graph.  Let the set be E.
# 3) Do following while E is not empty
# ...a) Pick an arbitrary edge (u, v) from set E and add 'u' and 'v' to result
# ...b) Remove all edges from E which are either incident on u or v.
# 4) Return result 

# How well the above algorithm perform? 
# It can be proved that the above approximate algorithm never finds a vertex cover 
# whose size is more than twice the size of the minimum possible vertex cover 

# Python3 program to print Vertex Cover
# of a given undirected graph 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph:

	def __init__(self, vertices):
		
		# No. of vertices
		self.V = vertices 
		
		# Default dictionary to store graph
		self.graph = defaultdict(list) 

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# The function to print vertex cover 
	def printVertexCover(self):
		
		# Initialize all vertices as not visited. 
		visited = [False] * (self.V)
		
		# Consider all edges one by one 
		for u in range(self.V):
			
			# An edge is only picked when 
			# both visited[u] and visited[v] 
			# are false
			if not visited[u]:
				
				# Go through all adjacents of u and 
				# pick the first not yet visited 
				# vertex (We are basically picking
				# an edge (u, v) from remaining edges. 
				for v in self.graph[u]:
					if not visited[v]:
						
						# Add the vertices (u, v) to the
						# result set. We make the vertex
						# u and v visited so that all 
						# edges from/to them would 
						# be ignored 
						visited[v] = True
						visited[u] = True
						break

		# Print the vertex cover 
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
				
		print()

# Driver code

# Create a graph given in 
# the above diagram 
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(3, 4) 
g.addEdge(4, 5) 
g.addEdge(5, 6) 

g.printVertexCover()

# This code is contributed by Prateek Gupta
