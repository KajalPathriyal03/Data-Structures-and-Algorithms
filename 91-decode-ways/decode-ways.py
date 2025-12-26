class Solution:
    def rec(self, i, s):
        if i==len(s):
            return 1 
        if s[i]=="0":
            return 0
        if i in self.dp:
            return self.dp[i]
        ans=0
        ans=self.rec(i+1, s)
        if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
            ans+=self.rec(i+2, s)
        self.dp[i]= ans 
        return self.dp[i]
    def numDecodings(self, s: str) -> int:
        self.dp={}
        return self.rec(0, s)
        