class UnionFind:
    def __init__(self, n):
        self.par=list(range(n))
        self.rank=[0 for _ in range(n)]
    
    def findUpar(self, node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def unionByRank(self, u, v):
        root_u=self.findUpar(u)
        root_v=self.findUpar(v)
        if root_u==root_v: return False
        if self.rank[root_u]<self.rank[root_v]:
            self.par[root_u]=root_v
        elif self.rank[v]<self.rank[root_u]:
            self.par[root_v]=root_u
        else:
            self.par[root_v]=root_u
            self.rank[root_u]+=1
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda edge: edge[2])

        mstWei=0
        uf=UnionFind(n)

        for u, v, wt, i in edges:
            if uf.findUpar(u)!=uf.findUpar(v):
                mstWei+=wt
                uf.unionByRank(u, v)

        critical, pseudo=[] ,[]

        for i in range(len(edges)):
            weight_without = 0
            edges_count = 0
            uf_without = UnionFind(n)
            for j in range(len(edges)):
                if i == j: 
                    continue
                u, v, wt, _ = edges[j]
                if uf_without.unionByRank(u, v):
                    weight_without += wt
                    edges_count += 1
            
    
            if edges_count < n - 1 or weight_without > mstWei:
                critical.append(edges[i][3])
                continue 

            uf_with = UnionFind(n)
            u_i, v_i, wt_i, original_index_i = edges[i]
            uf_with.unionByRank(u_i, v_i)
            weight_with = wt_i 
            for j in range(len(edges)):
                u, v, wt, _ = edges[j]
                if uf_with.unionByRank(u, v):
                    weight_with += wt
            
            if weight_with == mstWei:
                pseudo.append(original_index_i)

        return [critical, pseudo]
        
        