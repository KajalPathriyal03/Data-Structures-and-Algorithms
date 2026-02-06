class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[[1, 0], [-1, 0],[0, -1], [0, 1]]
        rows, cols=len(matrix),len(matrix[0])

        adj=defaultdict(list)
        ind=[[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                for x, y in directions:
                    newx=row+x
                    newy=col+y
                    if newx>=0 and newx<rows and newy>=0 and newy<cols and matrix[newx][newy]>matrix[row][col]:
                        adj[(row, col)].append((newx, newy))
                        ind[newx][newy]+=1
            
        queue=deque()
        for row in range(rows):
            for col in range(cols):
                if ind[row][col]==0:
                    queue.append((row, col))

        ans=0
        while queue:
            for i in range(len(queue)):
                row, col=queue.popleft()
                for newx, newy in adj[(row, col)]:
                    ind[newx][newy]-=1
                    if ind[newx][newy]==0:
                        queue.append((newx, newy))
            ans+=1
        return ans 


        

        