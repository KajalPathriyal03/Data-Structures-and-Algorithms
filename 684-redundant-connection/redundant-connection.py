class UnionFind:
    def __init__(self, n):
        self.par=[i for i in range(n)]
        self.rank=[0 for _ in range(n)]

    def findUpar(self, node):
        if self.par[node]==node:
            return node

        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def union(self, u, v):
        root_u=self.findUpar(u)
        root_v=self.findUpar(v)

        if root_u==root_v:
            return 

        if self.rank[root_u]<self.rank[root_v]:
            self.par[root_u]=root_v

        elif self.rank[root_v]<self.rank[root_u]:
            self.par[root_v]=root_u

        else:
            self.par[root_v]=root_u
            self.rank[root_u]+=1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        ds=UnionFind(n+1)
        ans=[]
        for u, v in edges:
            if ds.findUpar(u)==ds.findUpar(v):
                ans=[u, v]
            else:
                ds.union(u, v)
        return ans 

        