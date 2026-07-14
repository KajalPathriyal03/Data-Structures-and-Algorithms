class Solution:
    def dfs(self, ind, target, nums):
        if ind>=len(nums):
            return float('inf')
        if target<0: return float('inf')
        if target==0:
            return 0
        if (ind, target) in self.dp:
            return self.dp[(ind, target)]
        notTake = self.dfs(ind+1, target, nums)
        take = float('inf')
        if target-nums[ind]>=0:
            take= 1+ self.dfs(ind, target-nums[ind], nums)
        self.dp[(ind, target)]= min(take, notTake)
        return self.dp[(ind, target)]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp={}
        ans= self.dfs(0, amount, coins)
        if ans==float('inf'): return -1 
        return ans 
        