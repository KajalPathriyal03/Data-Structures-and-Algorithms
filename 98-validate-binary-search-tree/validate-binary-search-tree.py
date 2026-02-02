# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, left, right):
        if not root: return True
        if not (root.val<right and root.val>left):
            return False 
        leftSide=self.inorder(root.left, left, root.val)
        rightSide=self.inorder(root.right, root.val, right)
        return leftSide and rightSide

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root, float('-inf'), float('inf'))
        