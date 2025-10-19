# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, cur):
        if not root: return 0
        cur=cur*10+(root.val)
        if root.left==None and root.right==None:
            return cur
        l=self.solve(root.left, cur)
        r=self.solve(root.right, cur)
        return l+r


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = self.solve(root, 0)
        return ans 
        