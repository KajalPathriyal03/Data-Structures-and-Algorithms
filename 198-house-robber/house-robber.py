class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]=maximum stolen money till house i
        dp=[-1 for _ in range(len(nums)+1)]
        dp[0]=0
        dp[1]=nums[0]
        for i in range(1, len(nums)):
            dp[i+1]=max(dp[i-1]+nums[i], dp[i])
        # print(dp)
        return dp[len(nums)]
        