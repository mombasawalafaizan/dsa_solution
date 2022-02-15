# DFS approach
def dfs(s, vis, graph):
    vis[s] = True
    if s in graph:
        for adj in graph[s]:
            if vis[adj] or dfs(adj, vis, graph):
                return True
    vis[s] = False
    return False

def isCyclic(n, graph):
    vis = [False] * n
    for u in graph:
        if vis[u] == False:
            if dfs(u, vis, graph):
                return 1
    return 0




# BFS approach
def isCycleExist(n,graph):

	# Create a vector to store indegrees of all 
	# vertices. Initialize all indegrees as 0. 
	in_degree=[0]*n

	# Traverse adjacency lists to fill indegrees of 
	# vertices. This step takes O(V+E) time
	for i in range(n):
		for j in graph[i]:
			in_degree[j]+=1
	
	# Create an queue and enqueue all vertices with 
	# indegree 0
	queue=[]
	for i in range(n):
		if in_degree[i]==0:
			queue.append(i)
	
	# Initialize count of visited vertices
	cnt=0

	# One by one dequeue vertices from queue and enqueue 
	# adjacents if indegree of adjacent becomes 0 
	while(queue):

		# Extract front of queue (or perform dequeue) 
		# and add it to topological order 
		nu=queue.pop(0)

		# Iterate through all its neighbouring nodes 
		# of dequeued node u and decrease their in-degree 
		# by 1 
		for v in graph[nu]:
			in_degree[v]-=1

			# If in-degree becomes zero, add it to queue
			if in_degree[v]==0:
				queue.append(v)
		cnt+=1

	# Check if there was a cycle 
	if cnt==n:
		return False
	else:
		return True