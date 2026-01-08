class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for _ in range(n+1)]
        poweroftwo=1
        for i in range(1, n+1):
            if poweroftwo*2==i:
                poweroftwo=i
            dp[i]=1+dp[i-poweroftwo]
        return dp

        