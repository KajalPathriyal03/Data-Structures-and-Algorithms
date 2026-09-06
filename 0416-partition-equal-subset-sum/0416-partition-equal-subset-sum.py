class Solution:
    def dfs(self, ind, nums, w):
        if w==0: 
            return True 
        if ind>=len(nums):
            return False 
        if (ind, w) in self.dp:
            return self.dp[(ind, w)]

        notTake = self.dfs(ind+1, nums, w)
        take =0 
        if nums[ind]<=w:
            take = self.dfs(ind+1, nums, w-nums[ind])
        self.dp[(ind, w)]= take or notTake
        return self.dp[(ind, w)]
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm & 1: return False 
        target=sm//2 
        self.dp={}
        return self.dfs(0, nums, target)

        