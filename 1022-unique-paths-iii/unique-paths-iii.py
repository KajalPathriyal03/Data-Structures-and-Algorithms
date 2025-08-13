class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m=len(grid), len(grid[0])
        if grid[0][0]==-1: return 0
        if grid[0][0]==2: return 1 

        def dfs(row, col, path_length):
            
            if grid[row][col] == 2:
                return 1 if path_length == empty_space else 0

            val = grid[row][col]
            grid[row][col] = -1
            
            ans = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                new_x, new_y=row+dr, col+dc
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y]!=-1:
                    ans += dfs(new_x, new_y, path_length + 1)

            grid[row][col] = val
            
            return ans

        empty_space=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    row, col=i, j
                if grid[i][j]!=-1:
                    empty_space+=1
        ans=dfs(row, col, 1)
        return ans 



  