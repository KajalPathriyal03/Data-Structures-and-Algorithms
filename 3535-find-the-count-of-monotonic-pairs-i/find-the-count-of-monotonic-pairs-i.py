class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod=10**9+7
        n=len(nums)
        dp={}

        def dfs(i, prev1, prev2):
            if i==n:
                return 1
            if (i, prev1, prev2) in dp:
                return dp[(i, prev1, prev2)]
            ans=0
            for j in range(prev1, nums[i]+1):
                x1=j
                x2=nums[i]-j
                if x1>=prev1 and x2<=prev2:
                    ans+=dfs(i+1, x1, x2)
            dp[(i, prev1, prev2)]=ans
            return dp[(i, prev1, prev2)]%mod
        ans=dfs(0, 0, 50)
        return ans
        