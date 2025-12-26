class Solution:
    def rec(self, i, j, s1, s2, s3):
        if i==len(s1) and j==len(s2):
            return True 
        if (i+j)==len(s3):
            return False
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        ans=False
        if i<len(s1) and s1[i]==s3[(i+j)]:
            ans=self.rec(i+1, j, s1, s2, s3)
        if ans==True:
            return True
        if j<len(s2) and s2[j]==s3[(i+j)]:
            ans=self.rec(i, j+1, s1, s2, s3)
        self.dp[(i, j)]= ans
        return self.dp[(i, j)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.dp={}
        if len(s1)+len(s2)<len(s3): return False
        return self.rec(0, 0, s1, s2, s3)
        