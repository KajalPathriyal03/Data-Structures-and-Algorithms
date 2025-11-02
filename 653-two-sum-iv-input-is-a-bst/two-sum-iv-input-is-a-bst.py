# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodes(self, root):
        if not root:
            return 
        
        self.nodes(root.left)
        self.st.append(root.val)
        self.nodes(root.right)
    def twoSum(self, nums, k):
        l, r=0, len(nums)-1
        while l<r:
            if nums[l]+nums[r]>k:
                r-=1
            
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                return True 
            
        return False 
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.st=[]
        self.nodes(root)
        return self.twoSum(self.st, k)
        
        