class Solution:
    def dfs(self, left, right):
        if left==None or right==None:
            return left==right
        if left.val != right.val:
            return False 
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.dfs(root.left, root.right)

        