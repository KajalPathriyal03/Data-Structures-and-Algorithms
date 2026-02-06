class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for u, v, wt in flights:
            adj[u].append((v, wt))
        dis=[float('inf') for _ in range(n)]
        dis[src]=0
        pq=deque()
        pq.append((0, src, 0))
        while pq:
            dist, node, stop = pq.popleft()
            
            if stop>k:
                continue

            for nei, wt in adj[node]:
                newDist=dist+wt
                if newDist<dis[nei]:
                    dis[nei]=newDist
                    newstop=stop+1
                    pq.append((dis[nei], nei, newstop))
        if dis[dst]==float('inf'):
            return -1
        return dis[dst]

        