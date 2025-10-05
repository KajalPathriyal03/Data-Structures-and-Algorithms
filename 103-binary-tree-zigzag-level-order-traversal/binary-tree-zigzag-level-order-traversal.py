# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        queue=deque()
        queue.append(root)
        flag=0
        while queue:
            sz=len(queue)
            level=[]
            while sz:
                node=queue.popleft()
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
                level.append(node.val)
                sz-=1
            if flag==0:
                ans.append(level.copy())
                flag=1
            else:
                ans.append(level[::-1])
                flag=0
        return ans 

