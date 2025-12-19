class Solution:
    def rec(self, i, j, grid):
        if i<0 or j<0 or i>=len(grid) or j >= len(grid[0]):
            return float('inf')
        if i==len(grid)-1 and j==len(grid[0])-1:
            return grid[i][j]
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        right=self.rec(i, j+1, grid)
        down=self.rec(i+1, j, grid)
        self.dp[(i, j)]= grid[i][j]+min(right,down)
        return self.dp[(i, j)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp={}
        ans=self.rec(0, 0, grid)
        return ans 