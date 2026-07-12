class Solution:
    def dfs(self, i, j, m, n):
        if i>=m or j>=n: return 0
        if i==m-1 and j==n-1:
            return 1 
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        down=self.dfs(i+1, j, m, n)
        right=self.dfs(i, j+1, m, n)
        self.dp[(i, j)]= down + right 
        return self.dp[(i, j)]
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp={}
        return self.dfs(0, 0, m, n)
        