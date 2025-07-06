class UnionFind:
    def __init__(self, n):
        self.par=list(range(n+1))
        self.rank=[0 for _ in range(n+1)]

    def findUpar(self, node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def union(self, u, v):
        root_u = self.findUpar(u)
        root_v = self.findUpar(v)
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            self.par[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.par[root_v] = root_u
        else:
            self.par[root_v] = root_u
            self.rank[root_u] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        ds=UnionFind(c)
        for u, v in connections:
            ds.union(u,v)
   
        component_heap = defaultdict(list)
        for station in range(1, c + 1):
            root = ds.findUpar(station)
            heapq.heappush(component_heap[root], station)
        

        flag=[1 for _ in range(c+1)]
        ans=[]
        for u, v in queries:
            
            if u==1:
                if flag[v]==1:
                    ans.append(v)
                else:
                    root=ds.findUpar(v)
                    heap=component_heap[root]
                    while heap and not flag[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)
            elif u==2:
                flag[v]=0
        return ans
                
                
        