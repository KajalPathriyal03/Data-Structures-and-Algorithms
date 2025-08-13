class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges):
            adj=defaultdict(list)
            ind=[0 for _ in range(k+1)]
            for u, v in edges:
                adj[u].append(v)
                ind[v]+=1
            
            queue=deque()
            for i in range(1, k+1):
                if ind[i]==0:
                    queue.append(i)
            sort=[]
            while queue:
                node=queue.popleft()
                sort.append(node)
                for nei in adj[node]:
                    ind[nei]-=1
                    if ind[nei]==0:
                        queue.append(nei)
            
            for i in range(1, k+1):
                if ind[i]!=0:
                    return []
            return sort

        row=topo(rowConditions)
        col=topo(colConditions)

        if len(row)==0 or len(col)==0: return []

        grid=[[0 for _ in range(k)]for _ in range(k)]
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i]==col[j]:
                    grid[i][j]=row[i]
        return grid





        