class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj = defaultdict(list)
        for i, ele in enumerate(edges):
            if ele == -1:
                continue
            else:
                adj[i].append(ele)

        def bfs(src, dis, check, ans):
            if check[src]: return 

            check[src]=True
            ans[src]=dis
            for nei in adj[src]:
                bfs(nei, dis+1, check, ans)

        ans1=[-1]*n
        ans2=[-1]*n

        vis=[False]*n
        bfs(node1, 0, vis, ans1)
        visited=[False]*n
        bfs(node2, 0, visited, ans2)
        print(ans1, ans2)

        ind=-1
        maxi = float("inf")
        for i in range(n):
            if ans1[i] == -1 or ans2[i] == -1: continue

            dist = max(ans1[i], ans2[i])
            if maxi > dist:
                maxi = dist
                ind = i
        return ind

