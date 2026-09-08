# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preorder, inorder, start, end,mp):
        if start>end: 
            return None 

        rootVal = preorder[self.ind]
        root=TreeNode(rootVal)
        i=mp[rootVal]
        self.ind+=1
        root.left=self.build(preorder, inorder, start, i-1, mp)
        root.right=self.build(preorder, inorder, i+1, end, mp)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp={}
        for i, ele in enumerate(inorder):
            mp[ele]=i
        
        self.ind=0
        return self.build(preorder, inorder, 0, len(inorder)-1, mp)
        