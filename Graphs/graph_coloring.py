from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def greedyColoring(self):
        result = [-1] * self.V
        available = [True] * self.V
        result[0] = 0
        for u in range(1, self.V):
            for adj in self.graph[u]:
                if result[adj] != -1:
                    available[result[adj]] = False
            
            cr = 0
            while cr < self.V:
                if available[cr]:
                    break
                cr += 1
            result[u] = cr
            for i in range(len(available)):
                available[i] = True
        
        for u in range(self.V):
            print("Vertex",u,"--->  Color",result[u])


if __name__ == "__main__":
    g1 = Graph(5)
    g1.addEdge(0, 1) 
    g1.addEdge(0, 2) 
    g1.addEdge(1, 2) 
    g1.addEdge(1, 3) 
    g1.addEdge(2, 3) 
    g1.addEdge(3, 4) 
    print('Coloring of graph 1: ')
    g1.greedyColoring()

    g2 = Graph(5)
    g2.addEdge(0, 1) 
    g2.addEdge(0, 2) 
    g2.addEdge(1, 2) 
    g2.addEdge(1, 4) 
    g2.addEdge(2, 4) 
    g2.addEdge(4, 3) 
    print('Coloring of graph 1: ')
    g2.greedyColoring()