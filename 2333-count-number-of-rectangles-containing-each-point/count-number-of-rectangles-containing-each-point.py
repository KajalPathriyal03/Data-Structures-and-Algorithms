from sortedcontainers import SortedList
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n, m=len(rectangles), len(points)
        mp=defaultdict(SortedList)
        for l, h in rectangles:
            for i in range(1, h+1):
                mp[i].add(l)
        ans=[]
        for x, y in points:
            cnt=0
            ind=bisect.bisect_left(mp[y], x)
            ln=len(mp[y])
            cnt+=(ln-ind)
            ans.append(cnt)
            
        return ans 