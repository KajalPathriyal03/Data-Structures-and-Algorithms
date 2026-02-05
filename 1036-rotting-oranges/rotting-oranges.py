class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        queue=deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append((row, col, 0))
        ans=0
        while queue:
            row, col, time=queue.popleft()
            ans=time 
            directions=[[1, 0], [-1, 0], [0,1], [0, -1]]
            for x, y in directions:
                newx=row+x
                newy=col+y
                if newx>=0 and newx<rows and newy>=0 and newy<cols and grid[newx][newy]==1:
                    grid[newx][newy]=2
                    queue.append((newx, newy, time+1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1
        
        return ans 

        