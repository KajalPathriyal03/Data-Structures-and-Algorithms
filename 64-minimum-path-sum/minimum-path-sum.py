class Solution:
    def dfs(self, row, col, grid):
        if row>=len(grid) or col>=len(grid[0]):
            return float('inf')

        if row==len(grid)-1 and col==len(grid[0])-1:
            return grid[row][col]

        if (row, col) in self.dp:
            return self.dp[(row, col)]

        right=grid[row][col]+self.dfs(row, col+1, grid)
        down=grid[row][col]+self.dfs(row+1, col, grid)

        self.dp[(row, col)]= min(right, down)
        return self.dp[(row, col)]
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp={}
        return self.dfs(0, 0, grid)
        