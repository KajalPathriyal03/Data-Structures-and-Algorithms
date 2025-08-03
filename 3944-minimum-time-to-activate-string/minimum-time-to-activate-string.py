from sortedcontainers import SortedList
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n=len(s)
        st=SortedList([-1, n])
        print(st)
        cnt=0
        for t in range(len(order)):
            pos=order[t]
            l=bisect.bisect_right(st, pos)
            cnt+=(pos-st[l-1])*(st[l]-pos)
            if cnt>=k:
                return t
            st.add(pos)
        return -1
            
            
            
            
            
                
                
                