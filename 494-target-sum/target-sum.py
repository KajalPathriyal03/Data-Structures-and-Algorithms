class Solution:
    def rec(self, ind, nums,target, sm):
        if ind>=len(nums) and sm==target:
            return 1
        if ind>=len(nums): return 0
        if (ind, sm) in self.dp:
            return self.dp[(ind, sm)]

        add=self.rec(ind+1, nums, target, sm+nums[ind])
        subtract=self.rec(ind+1, nums, target, sm-nums[ind])
        self.dp[(ind, sm)]= add+subtract
        return self.dp[(ind, sm)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp={}
        return self.rec(0, nums, target, 0)
        
        