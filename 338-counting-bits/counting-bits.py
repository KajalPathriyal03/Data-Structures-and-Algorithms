class Solution:
    def cntOnes(self, n):
        cnt=0
        while n:
            n=n&(n-1)
            cnt+=1
        return cnt
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        for i in range(1, n+1):
            cnt=self.cntOnes(i)
            ans.append(cnt)
        return ans

        