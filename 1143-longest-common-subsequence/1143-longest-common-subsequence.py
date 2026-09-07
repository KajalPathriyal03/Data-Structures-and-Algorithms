class Solution:
    def dfs(self, i, j, s1, s2):
        if i>=len(s1) or j>=len(s2):
            return 0
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        if s1[i]==s2[j]:
            self.dp[(i, j)]= 1+self.dfs(i+1, j+1, s1, s2)
        else:
            self.dp[(i, j)]= max(self.dfs(i+1, j, s1, s2), self.dfs(i, j+1, s1, s2))
        return self.dp[(i, j)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp={}
        return self.dfs(0, 0, text1, text2)
        