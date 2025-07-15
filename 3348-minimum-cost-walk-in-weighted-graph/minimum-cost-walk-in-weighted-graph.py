class UnionFind:
    def __init__(self, n):
        self.par=list(range(n))
        self.rank=[0]*n
    
    def findUpar(self, node):
        if self.par[node]==node: return node
        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def union(self, u, v):
        root_u=self.findUpar(u)
        root_v=self.findUpar(v)
        if root_u==root_v: return
        if self.rank[root_u]<self.rank[root_v]:
            self.par[root_u]=root_v
        elif self.rank[root_v]<self.rank[root_u]:
            self.par[root_v]=root_u
        else:
            self.par[root_v]=root_u
            self.rank[root_u]+=1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        ds=UnionFind(n)
        cost=[-1]*n
        for u, v, wt in edges:
            ds.union(u,v)

        for u, v, wt in edges:
            root_u=ds.findUpar(u)
            cost[root_u] &= wt

        ans=[]
        for u, v in query:
            root_u=ds.findUpar(u)
            root_v=ds.findUpar(v)

            if root_u != root_v:
                ans.append(-1)
            else:
                ans.append(cost[root_u])
        return ans
