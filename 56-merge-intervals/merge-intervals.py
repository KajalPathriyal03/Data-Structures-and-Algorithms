class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        ans=[]
        ans.append(intervals[0])
        for start, end in intervals[1:]:
            last=ans[-1][1]
            if last>=start:
                ans[-1][1]=max(end, last)
            else:
                ans.append([start, end])
        return ans 

        