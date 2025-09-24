class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        zeroes, ones, twos=0, 0,0
        n=len(grid)
        ways=[[0, 1], [0,2], [1, 0], [1, 2], [2, 0], [2, 1]]
        dis=[[-1 for _ in range(n)] for _ in range(n)]
        mini=float('inf')
        for p, s in ways:
            mid=n//2
            cnt=0
            for i in range(n):
                for j in range(n):
                    dis[i][j]=s
                    if i<mid:
                        if i==j:  
                            dis[i][j]=p
                        elif j==n-i-1:
                            dis[i][j]=p
                    else:
                        if j==mid:
                            dis[i][j]=p
            for i in range(n):
                for j in range(n):
                    if dis[i][j]!=grid[i][j]:
                        cnt+=1
            mini=min(mini, cnt)
            
        return mini                    
                        
            
        