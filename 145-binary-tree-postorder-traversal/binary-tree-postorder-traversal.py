# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root==None:
            return
        self.solve(root.left)
        self.solve(root.right)
        self.ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.solve(root)
        return self.ans 