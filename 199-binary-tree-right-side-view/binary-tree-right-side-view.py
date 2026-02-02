# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue=deque()
        queue.append(root)
        ans=[]
        while queue:
            sz=len(queue)
            last=None
            while sz:
                node=queue.popleft()
                last=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sz-=1
            ans.append(last)
        return ans 
        