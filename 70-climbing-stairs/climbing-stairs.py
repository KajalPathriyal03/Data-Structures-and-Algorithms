class Solution:
    def rec(self, n):
        if n<=2: return n 
        if n in self.dp:
            return self.dp[n]
        self.dp[n]= self.rec(n-1)+self.rec(n-2)
        return self.dp[n]
    def climbStairs(self, n: int) -> int:
        self.dp={}
        return self.rec(n)

        