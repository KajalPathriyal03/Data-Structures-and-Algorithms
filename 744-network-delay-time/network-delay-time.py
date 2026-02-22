class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u, v, wt in times:
            adj[u].append((v, wt))
        dis=[float('inf') for _ in range(n+1)]
        pq=[]
        dis[k]=0
        heappush(pq, (0, k))
        ans = -1
        while pq:
            dist, node=heappop(pq)
            for nei,wt in adj[node]:
                newWt=dist+wt
                if dis[nei]> newWt:
                    dis[nei]=newWt
                    heappush(pq,(dis[nei], nei))

        ans=max(dis[1:])
        if ans == float('inf'): return -1
        return ans 


        