class Solution:
    def bfs(self, queue, heights, vis):
        ans=[]
        rows, cols=len(heights), len(heights[0])
        while queue:
            r, c=queue.popleft()
            ans.append((r, c))
            directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x,y in directions:
                newx, newy=x+r, y+c

                if newx>=0 and newy>=0 and newx<rows and newy<cols and (newx, newy) not in vis and heights[newx][newy]>=heights[r][c]:
                    vis.add((newx, newy))
                    queue.append((newx, newy))

        return vis


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols=len(heights), len(heights[0])
        pacific_queue=deque()
        atlantic_queue=deque()
        pacific=set()
        atlantic=set()

        for r in range(rows):
            pacific_queue.append((r, 0))
            pacific.add((r, 0))

            atlantic_queue.append((r, cols-1))
            atlantic.add((r,cols-1))

        for c in range(cols):
            pacific_queue.append((0, c))
            pacific.add((0, c))

            atlantic_queue.append((rows-1, c))
            atlantic.add((rows-1, c))

        self.bfs(pacific_queue, heights, pacific)
        self.bfs(atlantic_queue, heights, atlantic)

        intersac=pacific.intersection(atlantic)
        return list(intersac)
        

        



        