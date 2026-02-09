class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        queue=deque()

        rows, cols=len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    queue.append((i, j))

        while queue:
            r, c=queue.popleft()

            for i in range(rows):
                matrix[i][c]=0

            for j in range(cols):
                matrix[r][j]=0

        
        