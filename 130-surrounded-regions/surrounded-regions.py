class Solution:
    def dfs(self, r, c, grid):
        self.vis.add((r, c))
        directions=[[1,0], [-1,0], [0, 1], [0, -1]]
        for x, y in directions:
            newx=x+r
            newy=y+c
            if newx>=0 and newx<len(grid) and newy>=0 and newy<len(grid[0]) and grid[newx][newy]!="X" and (newx,newy) not in self.vis:
                grid[newx][newy]="NA"
                self.dfs(newx, newy, grid)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols=len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O" and (i==0 or i==rows-1 or j==0 or j==cols-1):
                    self.vis=set()
                    board[i][j]="NA"
                    self.dfs(i, j, board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="NA":
                    board[i][j]="O"
        



        