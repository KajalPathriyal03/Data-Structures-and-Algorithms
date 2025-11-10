class Solution:
    def dfs(self, i, j, grid, n, m):
        if i>=n or j>=m: return 
        directions=[[1, 0], [0,1], [0,-1], [-1, 0]]
        for x, y in directions:
            newx=i+x
            newy=j+y
            if newx<n and newy<m and newx>=0  and newy>=0 and grid[newx][newy]=="1":
                grid[newx][newy]="0"
                self.dfs(newx, newy, grid, n, m)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m=len(grid), len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    ans+=1
                    self.dfs(i, j, grid, n, m)
        return ans 

        