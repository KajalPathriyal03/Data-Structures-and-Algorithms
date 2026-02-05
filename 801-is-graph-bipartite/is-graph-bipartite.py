class Solution:
    def dfs(self, node, cur, graph):
        self.color[node]=cur 
        for nei in graph[node]:
            if self.color[nei]==-1:
                if self.dfs(nei, not cur, graph)==False:
                    return False
            else:
                if self.color[nei]==cur:
                    return False 
        return True 

    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True 
        self.color=[-1 for _ in range(len(graph))]
        for node in range(len(graph)):
            if self.color[node]==-1:
                if self.dfs(node, 0, graph)==False:
                    return False 
        return True 


        