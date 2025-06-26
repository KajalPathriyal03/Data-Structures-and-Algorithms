class UnionFind:
    # // Kajal
    def __init__(self, size):
        self.parent = list(range(size))  
        self.rank = [0] * size  
        self.components=size
   
    def findUPar(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
   
    def unionByRank(self, u, v):
        root_u = self.findUPar(u)
        root_v = self.findUPar(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        self.components-=1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob=UnionFind(n), UnionFind(n)
        cnt=0

        for t, u, v in edges:
            if t==3:
                if alice.unionByRank(u-1, v-1):
                    bob.unionByRank(u-1, v-1)
                    cnt+=1
        for t, u, v in edges:
            if t==1:
                if alice.unionByRank(u-1, v-1):
                    cnt+=1
            if t==2:
                if bob.unionByRank(u-1, v-1):
                    cnt+=1 
        if alice.components==1 and bob.components==1:
            return len(edges)-cnt
        return -1



        