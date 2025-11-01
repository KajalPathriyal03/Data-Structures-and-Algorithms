class Solution:
    def dfs(self, grid, i, j, n, m):
        if i<0 or j<0 or i>=n or j>=m:
            return float('inf')
        if i==n-1 and j==m-1:
            print(grid[i][j])
            return grid[i][j]
        if (i, j)  in self.dp:
            return self.dp[(i, j)]
        right=self.dfs(grid, i, j+1, n, m)
        left=self.dfs(grid, i+1, j, n, m)
        
        self.dp[(i, j)]= grid[i][j]+min(right, left)
        return self.dp[(i, j)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp={}
        self.ans=float('inf')
        n, m=len(grid), len(grid[0])
        self.vis=set()
        # self.dfs(grid, 0, 0, n, m, 0)
        return self.dfs(grid, 0, 0, n, m)

        