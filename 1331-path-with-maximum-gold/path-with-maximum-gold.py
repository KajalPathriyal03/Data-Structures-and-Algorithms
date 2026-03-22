class Solution:
    def rec(self, r, c, grid):
        rows, cols=len(grid), len(grid[0])
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r, c) in self.vis:
            return 0
        cur=grid[r][c]
        grid[r][c]=0
        maxi=cur
        directions=[[1, 0], [0, 1], [0, -1], [-1, 0]]
        for x, y in directions:
            newx, newy=x+r, y+c
            maxi=max(maxi, cur+self.rec(newx, newy, grid))
        grid[r][c]=cur 
        return maxi
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid=grid
        rows, cols=len(grid), len(grid[0])
        res=0
        for i in range(rows):
            for j in range(cols):
                self.vis=set()
                newGrid=self.grid
                if newGrid[i][j]!=0:
                    cur=self.rec(i, j, newGrid)
                    res=max(res, cur)
        return res

        