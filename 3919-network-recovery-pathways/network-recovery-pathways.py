class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        adj=defaultdict(list)
        for u, v, wt in edges:
            if online[u]!=False and online[v]!=False:
                adj[u].append((v, wt))
        n=len(online)
        def dikstra(mid):
            pq=[]
            heappush(pq, (0, 0))
            dis=[1e18 for _ in range(n)]
            dis[0]=0
            while pq:
                dist, node=heappop(pq)
                if dist>dis[node]: continue
                if node==n-1:
                    return dist 
                for nei, wt in adj[node]:
                    if wt<mid: continue
                    if dis[nei]>dist+wt:
                        dis[nei]=dist+wt
                        heappush(pq, (dis[nei], nei))

            return dis[n-1]


        l, r=0, int(1e9)
        mini=-1
        while l<=r:
            mid=r-(r-l)//2
            ans=dikstra(mid)
            if ans <= k:
                mini=mid
                l=mid+1
            else:
                r=mid-1
        return mini
                
        
                
            
        