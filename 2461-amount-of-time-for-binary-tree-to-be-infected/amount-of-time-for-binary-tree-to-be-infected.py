# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 
        if root.left:
            self.adj[root.val].append(root.left.val)
            self.adj[root.left.val].append(root.val)
        if root.right:
            self.adj[root.val].append(root.right.val)
            self.adj[root.right.val].append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.adj=defaultdict(list)
        self.dfs(root)
        t=-1
        queue=deque()
        queue.append(start)
        vis=set()
        while queue:
            sz=len(queue)
            while sz:
                node=queue.popleft()
                vis.add(node)
                for nei in self.adj[node]:
                    if nei not in vis:
                        queue.append(nei)
                sz-=1
            t+=1
            
        return t



        