class Solution:
    def dfs(self, row, col):
        if row>=len(self.grid) or row<0 or col>=len(self.grid[0]) or col<0 or self.grid[row][col]=='0':
            return 
        self.grid[row][col]='0'
        directions=[[1, 0],[-1,0], [0, 1], [0, -1]]
        for x, y in directions:
            newx=row+x
            newy=col+y
            self.dfs(newx, newy)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        self.grid=grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col]=='1':
                    ans+=1
                    self.dfs(row, col)
        return ans
        
        