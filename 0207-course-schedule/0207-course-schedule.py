class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        ind=[0 for _ in range(n) ]
        adj=defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            ind[v]+=1
        queue=deque()
        for i in range(n):
            if ind[i]==0:
                queue.append(i)

        ans = []
        while queue:
            node=queue.popleft()
            ans.append(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    queue.append(nei)
        if len(ans)==n: return True 
        return False 

