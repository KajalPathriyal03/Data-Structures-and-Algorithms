class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color: return image 
        col=image[sr][sc]
        queue=deque()
        vis=set()
        queue.append((sr, sc))
        vis.add((sr, sc))
        while queue:
            r, c= queue.popleft()
            image[r][c]=color
            directions=[[1, 0], [0, 1], [-1, 0], [0, -1]]
            for x, y in directions:
                newx=r+x
                newy=c+y
                if newx>=0 and newx<len(image) and newy>=0 and newy<len(image[0]) and (newx, newy) not in vis and image[newx][newy]==col:
                    vis.add((newx, newy))
                    queue.append((newx, newy))
        return image
        

        