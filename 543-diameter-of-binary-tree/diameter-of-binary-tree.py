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
        lh=self.dfs(root.left)
        rh=self.dfs(root.right)
        self.maxi=max(self.maxi, lh+rh)
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        self.dfs(root)
        return self.maxi

