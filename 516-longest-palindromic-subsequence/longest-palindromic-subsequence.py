class Solution:
    def rec(self, i, j, s1, s2):
        if i>=len(s1) or j>=len(s2):
            return 0
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        ans=0
        if s1[i]==s2[j]:
            ans=1+self.rec(i+1, j+1, s1, s2)
        else:
            one=self.rec(i, j+1, s1, s2)
            two=self.rec(i+1, j, s1, s2)
            ans=max(one, two)
        
        self.dp[(i, j)]= ans 
        return self.dp[(i, j)]

    def lcs(self, s, target):
        self.dp={}
        ans=self.rec(0, 0, s, target)
        return ans 
        
    def longestPalindromeSubseq(self, s: str) -> int:
        target=s[::-1]
        return self.lcs(s, target)

        