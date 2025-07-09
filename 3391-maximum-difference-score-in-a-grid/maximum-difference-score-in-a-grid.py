class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m=len(grid), len(grid[0])
        dis=[[0 for _ in range(m)] for _ in range(n)]
        dis[0][0]=grid[0][0]
        for j in range(1, m):
            dis[0][j]=min(dis[0][j-1], grid[0][j])
        for i in range(1, n):
             dis[i][0]=min(dis[i-1][0], grid[i][0])
        for i in range(1, n):
            for j in range(1, m):
                dis[i][j]=min(grid[i][j], dis[i-1][j], dis[i][j-1])
        maxi=float('-inf')
        print(dis)
        for i in range(n-1, -1, -1):
            for j in range(m-1,-1, -1):
                b=float('inf')
                if i-1>=0: b=min(b, dis[i-1][j])
                if j-1>=0: b=min(b, dis[i][j-1])
                maxi=max(maxi, grid[i][j]-b)
        return maxi

        
                
                
                
                
            
            
            
        