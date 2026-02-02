# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPath(self, root, target):
        if not root: return 
        if root.val==target:
            self.ans+=1
        
        self.findPath(root.left, target-root.val)
        self.findPath(root.right, target-root.val)

    def preorder(self, root, target):
        if not root: return 
        self.findPath(root, target)
        self.preorder(root.left, target)
        self.preorder(root.right, target)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0
        self.preorder(root, targetSum)
        return self.ans

        