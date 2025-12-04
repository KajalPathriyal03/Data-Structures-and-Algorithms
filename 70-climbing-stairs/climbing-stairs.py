class Solution:
    def rec(self, n):
        if n==0:
            return 1
        if n<0:
            return 0
        add_1=self.rec(n-1)
        add_2=self.rec(n-2)
        return add_1+add_2

    def climbStairs(self, n: int) -> int:
        f,s=1,1
        if n==0 or n==1: return f
        for i in range(2, n+1):
            cur=f+s
            f=s
            s=cur 
        return s

        