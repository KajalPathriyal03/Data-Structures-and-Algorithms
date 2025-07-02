class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums=[(nums[i]%k) for i in range(n)]        
        dp=[[0 for _ in range(k)] for _ in range(n)]
        last={}
        for i in range(k):
            last[i]=-1
        ans=0
        for i in range(n): 
            for y in range(k):
                if last[y]==-1:
                    dp[i][y]=1
                else:
                    dp[i][y]=dp[last[y]][nums[i]]+1
                ans=max(ans, dp[i][y])
            last[nums[i]]=i
        return ans