class Solution:
    def rec(self, i, j, s):
        if i>j:
            return 0
        if i==j:
            return 1
        if (i,j) in self.dp:
            return self.dp[(i, j)]
        ans = 0
        if s[i]==s[j]:
            ans=2+self.rec(i+1, j-1, s)
        else:
            one=self.rec(i+1, j, s)
            two=self.rec(i,j-1, s)
            ans=max(one,two)
        self.dp[(i, j)]= ans 
        return self.dp[(i, j)]

    def longestPalindromeSubseq(self, s: str) -> int:
        self.dp={}
        return self.rec(0, len(s)-1, s)
        