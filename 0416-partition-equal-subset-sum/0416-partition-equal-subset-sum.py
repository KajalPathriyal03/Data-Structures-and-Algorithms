class Solution:
    def dfs(self, i, nums, w):
        if w==0: return True 
        if i>=len(nums):
            return False 
        if (i, w) in self.dp:
            return self.dp[(i, w)]
            
        notTake = self.dfs(i+1, nums, w)
        take =0 
        if nums[i]<=w:
            take = self.dfs(i+1, nums, w-nums[i])
            
        self.dp[(i, w)]= take or notTake
        return self.dp[(i, w)]
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm & 1: return False 
        target=sm//2 
        self.dp={}
        return self.dfs(0, nums, target)

        