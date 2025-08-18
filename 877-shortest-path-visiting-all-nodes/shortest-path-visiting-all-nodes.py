class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        if n==1 or n==0: 
            return 0

        queue=deque()
        vis=set()

        for i in range(n):
            mask=(1<<i)
            queue.append((i, mask))
            vis.add((i, mask))

        all_vis=(1<<n)-1
        path=0
        while queue:
            ln=len(queue)
            path+=1
            while ln:
                node, mask=queue.popleft()
                # print(node, mask, path)
                for nei in graph[node]:
                    nxt_mask=mask | (1<<nei)
                    if nxt_mask==all_vis:
                        return path
                    if (nei, nxt_mask) not in vis:
                        vis.add((nei, nxt_mask))
                        queue.append((nei, nxt_mask))
                ln-=1
        return -1



        