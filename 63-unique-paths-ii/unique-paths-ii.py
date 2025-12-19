class Solution:
    def rec(self, i,j, grid, vis):
        if i<0 or j<0 or i>=len(grid) or j >= len(grid[0]) or (i, j) in vis or grid[i][j]==1:
            return 0
        if i==len(grid)-1 and j==len(grid[0])-1:
            return 1
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        vis.add((i, j))
        right=self.rec(i, j+1, grid, vis)
        down=self.rec(i+1, j, grid, vis)
        vis.remove((i, j))
        self.dp[(i, j)]= right+down
        return self.dp[(i, j)]


    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        self.dp={}
        vis=set()
        ans=self.rec(0, 0, grid, vis)
        return ans 
        