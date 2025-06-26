class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n=len(nums)
        dp=defaultdict(int)
        def dfs(mask, ops):
            if mask in dp:
                return dp[mask]

            for i in range(n):
                for j in range(i+1, n):
                    if (1<<i) & mask or (1<<j) & mask:
                        continue
                    newMask = mask | (1<<i) | (1<<j)
                    score=ops* math.gcd(nums[i], nums[j])
                    dp[mask]=max(dp[mask], score+dfs(newMask, ops+1))
            return dp[mask]

        return dfs(0, 1)
        