from typing import List


def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Bellman Ford
        cost = [float('inf')] * n
        cost[src] = 0
        for i in range(K+1):
            temp = cost[:]
            for f in flights:
                u, v, w = f[0], f[1], f[2]
                if cost[u] == float('inf'):
                    continue
                temp[v] = min(temp[v], cost[u] + w)
            cost = temp
        return cost[dst] if cost[dst]!=float('inf') else -1

        # Dijkstra's based
        # f = collections.defaultdict(dict)
        # for a, b, p in flights:
        #     f[a][b] = p
        # heap = [(0, src, K + 1)]
        # while heap:
        #     p, i, k = heapq.heappop(heap)
        #     if i == dst:
        #         return p
        #     if k > 0:
        #         for j in f[i]:
        #             heapq.heappush(heap, (p + f[i][j], j, k - 1))
        # return -1
        
        # BFS based
#         if src == dst: return 0
#         d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
#         for u, v, p in flights:
#             d[u] += [(v, p)]
    
#         q = [(src, -1, 0)]
        
#         while q:
#             pos, k, cost = q.pop(0)
#             if pos == dst or k == K: continue 
#             for nei, p in d[pos]:
#                 if cost + p >= seen[nei]:
#                     continue
#                 else:
#                     seen[nei] = cost+p
#                     q += [(nei, k+1, cost+p)]
                
#         return seen[dst] if seen[dst] < float('inf') else -1