# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target, cs, mp):
        if not root: return 

        cs+=root.val
        oldSum=cs-target
        self.ans+=mp.get(oldSum, 0)
        mp[cs]+=1

        self.dfs(root.left, target, cs, mp)
        self.dfs(root.right, target, cs, mp)

        mp[cs]-=1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0

        mp=defaultdict(int)
        mp[0]=1
        self.dfs(root, targetSum, 0, mp)
        return self.ans

        