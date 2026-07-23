# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ans=[]
        self.inorder(root)
        self.i=0

    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
    
    def next(self) -> int:
        res=self.ans[self.i]
        self.i+=1
        return res

    def hasNext(self) -> bool:
        if self.i<len(self.ans):
            return True 
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()