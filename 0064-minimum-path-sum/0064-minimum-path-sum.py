class Solution:
    def dfs(self, i, j, grid):
        if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0:
            return float('inf')
        
        if i==len(grid)-1 and j==len(grid[0])-1:
            return grid[i][j]

        if (i, j) in self.dp:
            return self.dp[(i, j)]

        right=self.dfs(i, j+1, grid)
        down=self.dfs(i+1, j, grid)
        self.dp[(i, j)]= grid[i][j]+min(right, down)
        return self.dp[(i, j)]
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp={}
        return self.dfs(0, 0, grid)
        