class UnionFind:
    def __init__(self,n):
        self.par=list(range(n))
        self.rank=[0 for _ in range(n)]

    def findUpar(self, node):
        if self.par[node]==node: return node
        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def union(self,u, v):
        root_u=self.findUpar(u)
        root_v=self.findUpar(v)
        if root_u==root_v: return False
        if self.rank[root_u]<self.rank[root_v]:
            self.par[root_u]=root_v
        elif self.rank[root_v]<self.rank[root_u]:
            self.par[root_v]=root_u
        else:
            self.par[root_v]=root_u
            self.rank[root_u]+=1
        return True
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: -x[2])
        print(edges)
        components=n
        ds=UnionFind(n)
        for u, v, t in edges:
            if ds.union(u, v): 
                components-=1
            if components<k:
                return t
        return 0


        