class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid), len(grid[0])
        queue=deque()
        ans=0
        print(queue)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i, j, 0))

        while queue:
            r, c, cost=queue.popleft()
            ans=cost
            directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in directions:
                newR, newC=r+x, c+y
                if newR>=0 and newC>=0 and newR<n and newC<m and grid[newR][newC]==1:
                    grid[newR][newC]=2
                    queue.append((newR, newC, cost+1)) 
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1

        return ans 

        