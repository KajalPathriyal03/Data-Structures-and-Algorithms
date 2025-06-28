
class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        n=len(edges)+1
        adj=defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        subtree_size=[0 for _ in range(n)]
        def dfs(node, par):
            sz=1
            for nei in adj[node]:
                if nei!=par:
                    sz+=dfs(nei, node)
            subtree_size[node]=sz
            return sz
        dfs(0, -1)

        cnt=0

        for i in range(n):
            flag=True
            prev_size=-1
            for nei in adj[i]:
                if subtree_size[nei]<subtree_size[i]:
                    if prev_size==-1:
                        prev_size=subtree_size[nei]
                    elif prev_size!=subtree_size[nei]:
                        flag=False
                        break
            if flag:
                cnt+=1
        return cnt