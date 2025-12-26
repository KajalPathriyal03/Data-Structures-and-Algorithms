class Solution:
    def rec(self, i, j, k, s1, s2, s3):
        if i==len(s1) and j==len(s2) and k==len(s3):
            return True 
        if k==len(s3):
            return False
        if (i, j, k) in self.dp:
            return self.dp[(i, j, k)]
        ans=False
        if i<len(s1) and s1[i]==s3[k]:
            ans=self.rec(i+1, j, k+1, s1, s2, s3)
        if ans==True:
            return True
        if j<len(s2) and s2[j]==s3[k]:
            ans=self.rec(i, j+1, k+1, s1, s2, s3)
        self.dp[(i, j, k)]= ans
        return self.dp[(i, j, k)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.dp={}
        if len(s1)+len(s2)<len(s3): return False
        return self.rec(0, 0, 0, s1, s2, s3)
        