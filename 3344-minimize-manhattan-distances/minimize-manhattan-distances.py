from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n=len(points)
        st1 = SortedList()
        st2 = SortedList()

        for x, y in points:
            st1.add(x + y)
            st2.add(x - y)

        ans = 1e9
        for x, y in points:
            p1, p2 = x + y, x - y

            st1.remove(p1)
            st2.remove(p2)

            dis1=st1[len(st1)-1]-st1[0]
            dis2=st2[len(st2)-1]-st2[0]

            res = max(dis1, dis2)
            ans = min(ans, res)

            st1.add(p1)
            st2.add(p2)

        return ans
            
            
            
                
        