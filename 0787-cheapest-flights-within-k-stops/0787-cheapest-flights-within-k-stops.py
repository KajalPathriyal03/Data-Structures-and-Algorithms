# from heappq import heapp
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src==dst: return 0
        adj=defaultdict(list)
        for u, v, wt in flights:
            adj[u].append((v, wt))

        dis=[float('inf') for _ in range(n)]
        dis[src]=0

        pq=deque()
        pq.append((k, 0, src))

        while pq:
            stops, dist, node = pq.popleft()
            if stops==-1:
                continue 
            for nei, wt in adj[node]:
                newWt=dist+wt
                if dis[nei]>newWt:
                    dis[nei]=newWt
                    pq.append((stops-1, dis[nei], nei))
        if dis[dst]==float('inf'):
            return -1
        return dis[dst]

        