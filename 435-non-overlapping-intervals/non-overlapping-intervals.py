# 1. if last[1]> cur[0]: overlapping 
# 2. last = which has minimum end 
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans=[intervals[0]]
        cnt=0
        for start,end in intervals[1:]:
            last=ans[-1]
            if last[1]>start:
                if last[1]>end:
                    ans.pop()
                    ans.append([start, end])
            else:
                ans.append([start, end])
        
        return len(intervals)-len(ans)
                
        