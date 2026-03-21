class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals 
        ans=[]
        
        intervals.sort()    
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            last=ans[-1]
            cur=intervals[i]
            if cur[0]<=last[1]:
                last[1]=max(cur[1], last[1])
            else:
                ans.append(cur)

        return ans 

                

            
        