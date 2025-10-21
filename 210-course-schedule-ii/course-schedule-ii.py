class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        ind=[0 for _ in range(n)]
        for v, u in edges:
            adj[u].append(v)
            ind[v]+=1
        print(ind)
        queue=deque()
        for i in range(n):
            if ind[i]==0:
                queue.append(i)
        ans=[]
        if len(queue)==0: 
            return ans 
        while queue:
            node=queue.popleft()
            ans.append(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    queue.append(nei)
        if len(ans)!=n:
            return []
        return ans 






