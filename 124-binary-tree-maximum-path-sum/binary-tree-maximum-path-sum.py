# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root==None:
            return 0
        leftMax=max(0, self.dfs(root.left))
        rightMax=max(0, self.dfs(root.right))
        self.maxi=max(self.maxi, leftMax+rightMax+root.val)
        return root.val+max(leftMax, rightMax)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        self.dfs(root)
        return self.maxi
        