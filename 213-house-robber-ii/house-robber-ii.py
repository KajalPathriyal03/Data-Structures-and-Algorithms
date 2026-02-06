class Solution:
    def dfs(self, ind, nums):
        if ind>=len(nums):
            return 0
        if ind in self.dp:
            return self.dp[ind]
        not_take=self.dfs(ind+1, nums)
        take =nums[ind]+self.dfs(ind+2, nums)
    
        self.dp[ind]= max(not_take, take)
        return self.dp[ind]
        
    def rob(self, nums: List[int]) -> int:
    
        self.dp={}
        ans1, ans2=0, 0
        n=len(nums)
        if n==1: return nums[0] #edge case 

        ans1=self.dfs(0, nums[:n-1])
        self.dp={}
        ans2=self.dfs(0, nums[1:])
        return max(ans1, ans2)
        