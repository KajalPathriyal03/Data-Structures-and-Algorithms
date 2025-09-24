class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n, m=len(grid), len(grid[0])
        ways=[[0, 1], [0, 2], [1,0], [1, 2],[2, 0], [2,1]]
        dis=[[-1 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        mini=n*n
        for p, s in ways:
            ans=0
            for row in range(n):
                for col in range(m):
                    dis[row][col]=p
                    mid=n//2
                    if row<mid:
                        if row==col:
                            dis[row][col]=s
                        elif col==n-row-1:
                            dis[row][col]=s
                    else:
                        if col==mid:
                            dis[row][col]=s
            print(dis)
            for row in range(n):
                for col in range(m):
                    if dis[row][col]!=grid[row][col]:
                        ans+=1
            mini=min(mini, ans)
                      
        return mini 