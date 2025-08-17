class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res=0
        adj=defaultdict(list)
        ind=[0 for _ in range(n)]
        if n<2: return 1
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            ind[u]+=1
            ind[v]+=1
        queue=deque()
        for i in range(n):
            if ind[i]==1:
                queue.append(i)
        ans=0
        while queue:
            ln=len(queue)
            for _ in range(ln):
                node=queue.popleft()
                ind[node]=0
                if values[node]%k==0:
                    ans+=1
                    for nei in adj[node]:
                        ind[nei]-=1
                        if ind[nei]==1:
                            queue.append(nei)
                else:
                    for nei in adj[node]:
                        ind[nei]-=1
                        values[nei]+=values[node]
                        if ind[nei]==1:
                            queue.append(nei)
        if ans==0: return 1
        return ans 


