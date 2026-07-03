# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, left, right):
        if left>right: return 
        mid=(left+right)//2 
        node=TreeNode(self.nums[mid])
        node.left=self.rec(left, mid-1)
        node.right=self.rec(mid+1, right)
        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums=nums 
        return self.rec(0, len(nums)-1)
        