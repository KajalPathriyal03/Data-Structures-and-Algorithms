class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        def bipartite(node, cur_color):
            colors[node]=cur_color
            for nei in adj[node]:
                if colors[nei]==colors[node]:
                    return False
                if colors[nei]==-1:
                    if bipartite(nei, 1-cur_color)==False:
                        return False
            return True 
        
        def bfs(node):
            queue=deque()
            queue.append(node)
            vis=set()
            vis.add(node)
            level=1
            while queue:
                ln=len(queue)
                while ln:
                    cur=queue.popleft()
                    for nei in adj[cur]:
                        if nei in vis:
                            continue
                        queue.append(nei)
                        vis.add(nei)
                    ln-=1
                level+=1
            return level-1
        def getMaxFromComponent(node, levels, vis):
            mx=levels[node]
            vis[node]=True
            for nei in adj[node]:
                if not vis[nei]:
                    mx=max(mx,getMaxFromComponent(nei, levels, vis))
            return mx
                
        for u, v in edges:
            u=u-1
            v=v-1
            adj[u].append(v)
            adj[v].append(u)
        
        colors=[-1 for _ in range(n)]
        for node in range(n):
            if colors[node]==-1:
                # flag=bipartite(node, 1)
                # print(flag)
                if bipartite(node, 1)==False:
                    return -1
        levels=[0 for _ in range(n)]
        for node in range(n):
            levels[node]=bfs(node)

        maxi=0
        print(levels)
        vis=[False for _ in range(n)]
        for node in range(n):
            if vis[node]==False:
                maxi+=getMaxFromComponent(node, levels, vis)
        return maxi




        
        