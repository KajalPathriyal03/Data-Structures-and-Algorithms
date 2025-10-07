# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        if root!=None and root.left==None and root.right==None:
            return True 
    def dfs(self, root):
        if root==None:
            return 
        self.ans.append(root.val)
        if self.isLeaf(root):
            st=""
            for ele in self.ans:
                st+=str(ele)+"->"
            self.res.append(st[:-2])
        else:
            self.dfs(root.left)
            self.dfs(root.right)
        self.ans.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res=[]
        self.ans=[]
        if root==None:
            return ans 
        self.dfs(root)
        return self.res 