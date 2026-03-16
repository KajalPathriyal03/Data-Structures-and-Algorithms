class Solution:
    def rec(self, ind, nums, target):
        if ind>=len(nums) and target==0:
            return 1

        if ind>=len(nums):
            return 0 

        if (ind, target) in self.dp:
            return self.dp[(ind, target)]

        plus=self.rec(ind+1, nums, target-nums[ind])
        minus=self.rec(ind+1, nums, target+nums[ind])
        self.dp[(ind, target)]= plus+minus
        return self.dp[(ind, target)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp={}
        return self.rec(0, nums, target)
        