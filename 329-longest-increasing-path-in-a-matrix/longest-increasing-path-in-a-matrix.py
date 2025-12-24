class Solution:
    def rec(self, i, j, grid):
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        res=1
        directions=[[1,0], [-1, 0], [0, 1], [0, -1]]
        for x, y in directions:
            newx=i+x
            newy=j+y
            if newx>=0 and newy>=0 and newx<len(grid) and newy < len(grid[0]) and grid[newx][newy]>grid[i][j]:
                res=max(res, 1+self.rec(newx, newy, grid))

        self.dp[(i, j)]= res
        return  self.dp[(i, j)]
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dp={}
        ans=-1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans=max(ans, self.rec(i, j, matrix))
        return ans 
                
        