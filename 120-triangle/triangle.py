class Solution:
    def rec(self, i, j, grid, row):
        if i==len(grid)-1 or j==len(grid)-1:
            return grid[i][j]
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        below=self.rec(i+1, j, grid, row+1)
        rightBelow=self.rec(i+1, j+1, grid, row+1)
        self.dp[(i, j)]= grid[i][j]+min(below, rightBelow)
        return self.dp[(i, j)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.dp={}
        ans=self.rec(0, 0, triangle, 0)
        return ans 
        