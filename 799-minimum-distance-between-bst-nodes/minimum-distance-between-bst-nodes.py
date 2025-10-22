# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root:
            self.solve(root.left)
            if self.pre!=-1:
                self.res=min(self.res, root.val-self.pre)
            self.pre=root.val
            self.solve(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res=float('inf')
        self.pre=-1
        self.solve(root)
        return self.res



        