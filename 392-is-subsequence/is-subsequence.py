class Solution:
    def rec(self, i, j, s, t):
        if i>=len(s):
            return True 
        if j>=len(t):
            return False
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        not_take=self.rec(i, j+1, s, t)
        take=False
        if s[i]==t[j]:
            take=self.rec(i+1, j+1, s, t)
        self.dp[(i, j)]= take or not_take
        return self.dp[(i, j)]
        
    def isSubsequence(self, s: str, t: str) -> bool:
        self.dp={}
        return self.rec(0, 0, s, t)