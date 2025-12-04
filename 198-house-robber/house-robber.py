class Solution:
    def rec(self, ind, nums):
        if ind >= len( nums):
            return 0
        if ind in self.dp:
            return self.dp[ind]
        not_take=self.rec(ind+1, nums)
        take=nums[ind]+self.rec(ind+2, nums)
        self.dp[ind]= max(take, not_take)
        return self.dp[ind]
    def rob(self, nums: List[int]) -> int:
        self.dp={}
        return self.rec(0, nums)
        