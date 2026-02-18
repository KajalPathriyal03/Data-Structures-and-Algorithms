class Solution:
    def isPossible(self, mid, intervals, newInterval):
        if mid==len(intervals):
            return False
        s1,e1=intervals[mid][0], intervals[mid][1]
        s2,e2=newInterval[0], newInterval[1]
        if s2<=e1:
            return True 
        return False 

    def merge(self, intervals):
        intervals.sort()
        nums=[intervals[0]]
        for i in range(1, len(intervals)):
            ls, le=nums[-1][0], nums[-1][1]
            if le>=intervals[i][0]:
                nums.pop()
                cs=min(ls, intervals[i][0])
                ce=max(le, intervals[i][1])
                nums.append([cs, ce])
            else:
                nums.append(intervals[i])
        return nums

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        nums=self.merge(intervals)
        print(nums)
        
        l, r=0, len(nums)-1
        ans=len(nums)
        while l<=r:
            mid=(l+r)//2
            if self.isPossible(mid, nums, newInterval):
                ans=mid 
                r=mid-1
                
            else:
                l=mid+1
        
        res=nums
        print(nums, ans)
        if ans==len(nums):
            res.append(newInterval)
            return res
        nums.append(newInterval)
        res=self.merge(nums)
    
        return res
        