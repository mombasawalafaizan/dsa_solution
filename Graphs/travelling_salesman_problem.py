from itertools import count, permutations

def findMinRoute(tsp):
    sum = 0
    counter = 0
    j = i = 0
    min = float('inf')
    visitedRouteList = []
    visitedRouteList.append(0)
    route = [0] * len(tsp)

    while i < len(tsp) and j < len(tsp[i]):
        # print(counter, i, j, visitedRouteList, route)
        if counter >= len(tsp[i])-1:
            break
        if j!=i and j not in visitedRouteList:
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1
        j += 1
        if j == len(tsp[i]):
            print(min)
            sum += min
            min = float('inf')
            visitedRouteList.append(route[counter]-1)
            j = 0
            i = route[counter]-1
            counter += 1

    i = route[counter-1] - 1

    for j in range(len(tsp)):
        if i!=j and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1
    sum += min
    return sum


# This function finds all possible permutations and
# keep track of min path
def travellingSalesmanProblem(graph, s, V): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = float('inf')
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 


if __name__ == "__main__":
    tsp = [
            [ -1, 10, 15, 20 ],
            [ 10, -1, 35, 25 ],
            [ 15, 35, -1, 30 ],
            [ 20, 25, 30, -1 ]
        ]
    # print(travellingSalesmanProblem(tsp, 0, 4))
    print(findMinRoute(tsp))