class UnionFind:
    def __init__(self, n):
        self.par=[x for x in range(n)]
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        ds=UnionFind(n)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    ds.union(i, j)
        ans=0
        for i in range(len(isConnected)):
            if ds.par[i]==i:
                ans+=1
        return ans 

        
        