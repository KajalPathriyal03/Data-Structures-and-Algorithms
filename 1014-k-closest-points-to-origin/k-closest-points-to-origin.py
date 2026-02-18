class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        for x, y in points:
            dist=sqrt((0-x)**2 + (0-y)**2)
            heappush(pq, (dist, [x, y]))
        ans=[]
        while pq and k>0:
            ans.append(heappop(pq)[1])
            k-=1
        return ans 


        