'''count squares with length'''
class Solution:
    def rec(self, i, j, grid):
        if i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0: return 0
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        right=self.rec(i, j+1, grid)
        below=self.rec(i+1, j, grid)
        diag=self.rec(i+1, j+1, grid)
        self.dp[(i, j)]= 1+min(right, below,diag)
        return self.dp[(i, j)]
    def countSquares(self, matrix: List[List[int]]) -> int:
        res=0
        self.dp={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    res+=self.rec(i, j, matrix)
        return res
        