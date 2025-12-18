class Solution:
    def rec(self, n):
        if n==0: return 0
        if n in self.dp:
            return self.dp[n]
        min_cnt=float('inf')
        i=1
        while i*i<=n:
            res=1+self.rec(n-i*i)
            min_cnt=min(min_cnt, res)
            i+=1
        
        self.dp[n]=min_cnt     
        return self.dp[n]  
    def numSquares(self, n: int) -> int:
        self.dp={}
        return self.rec(n)
