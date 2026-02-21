class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols=len(mat),len(mat[0])
        queue=deque()
        vis=set()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i, j))
                    vis.add((i, j))

        while queue:
            r, c =queue.popleft()
            directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in directions:
                newx, newy=r+x, c+y
                if newx>=0 and newy >=0 and newx<rows and newy<cols and (newx, newy) not in vis:
                    vis.add((newx,newy))
                    mat[newx][newy]+=mat[r][c]
                    queue.append((newx, newy))
        return mat

        