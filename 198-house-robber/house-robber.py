class Solution:
    def solve(self, nums, i):
        if i>=len(nums):
            return 0
        if i in self.dp:
            return self.dp[i]
        steal=nums[i]+self.solve(nums, i+2)
        skip=0+self.solve(nums, i+1)
        self.dp[i]= max(steal, skip)
        return self.dp[i]
    def rob(self, nums: List[int]) -> int:
        self.dp={}
        self.ans=self.solve(nums, 0)
        return self.ans
        