class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # dp[i]=minimum number of moves to build block till i
        n=len(target)
        dp=[float('inf') for _ in range(n)]
        dp[0]=target[0]
        for i in range(1, n):
            if target[i]>target[i-1]:
                dp[i]=dp[i-1]+target[i]-target[i-1]
            else:
                dp[i]=dp[i-1]
        # print(dp)
        return dp[n-1]

        