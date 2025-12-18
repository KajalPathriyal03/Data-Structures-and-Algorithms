class Solution:
    def rec(self, ind, nums, sm):
        if sm>=self.target or ind==len(nums):
            firstKnapsack=sm-nums[ind-1]
            secondKnapsack=self.total-firstKnapsack
            return abs(sm-(self.total-sm))
        if (ind, sm) in self.dp:
            return self.dp[(ind, sm)]
        not_take=self.rec(ind+1, nums, sm)
        take=self.rec(ind+1, nums, sm+nums[ind])
        self.dp[(ind, sm)]= min(not_take, take )
        return self.dp[(ind, sm)]

    def lastStoneWeightII(self, nums: List[int]) -> int:
        self.dp={}
        self.total=sum(nums)
        self.target=self.total//2
        ans=self.rec(0, nums, 0)
        return ans 
        
        
        