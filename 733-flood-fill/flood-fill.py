class Solution:
    def dfs(self, r, c, real, grid, color):
        grid[r][c]=color
        
        rows, cols=len(grid), len(grid[0])
        if r>=rows or c>=cols:
            return 
        directions =[[1, 0], [0, 1], [-1, 0], [0, -1]]
        for x, y in directions:
            newx, newy=r+x, y+c
            if newx>=0 and newx<rows and newy<cols and newy>=0 and grid[newx][newy]==real:
                self.dfs(newx, newy, real, grid, color)

        return grid

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        return self.dfs(sr, sc, image[sr][sc], image, color)

        