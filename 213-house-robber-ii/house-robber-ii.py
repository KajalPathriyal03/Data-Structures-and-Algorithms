class Solution:
    def rec(self, ind, nums):
        if ind >= len(nums):
            return 0
        if ind in self.dp:
            return self.dp[ind]
        not_take=self.rec((ind+1), nums)
        take=nums[ind]+self.rec((ind+2), nums)
        self.dp[ind]= max(take, not_take)
        return self.dp[ind]
    def rob(self, nums: List[int]) -> int:
        self.dp={}
        if len(nums)==1:
            return nums[0]
        arr=nums
        front=self.rec(0, arr[:len(nums)-1])
        self.dp={}
        back=self.rec(0, arr[1:])
        return max(front, back)
        