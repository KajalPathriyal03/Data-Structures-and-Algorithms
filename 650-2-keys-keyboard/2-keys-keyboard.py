class Solution:
    def recentFactor(self, cur):
        ans=-1
        for i in range(cur-1, -1, -1):
            if cur%i==0:
                ans=i
                break
        return ans 

    def solve(self, ind, n):
        if ind>n:
            return 
        divisor=self.recentFactor(ind)
        self.ans[ind]=self.ans[divisor]+ind//divisor
        self.solve(ind+1, n)

    def minSteps(self, n: int) -> int:
        self.ans=[0 for _ in range(n+1)]
        
        if n>=1:
            self.ans[1]=0
        if n>=2:
            self.ans[2]=2
        if n>=3:
            self.ans[3]=3
        if n>3:
            self.solve(4, n)
        return self.ans[n]



        
