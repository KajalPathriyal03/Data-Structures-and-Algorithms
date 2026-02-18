class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq=[]

        for i in range(len(heights)-1):
            dif=heights[i+1]-heights[i]
            if dif>0:
                if len(pq)<ladders:
                    heappush(pq, dif)

                else:
                    if not pq or dif<=pq[0]:
                        bricks-=dif

                    else:
                        mini=heappop(pq)
                        heappush(pq, dif)
                        bricks-=mini

                    if bricks<0:
                        return i

        return len(heights)-1
        