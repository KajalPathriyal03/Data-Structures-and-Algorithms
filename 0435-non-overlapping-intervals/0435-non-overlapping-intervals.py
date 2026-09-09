class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x:x[1])
        ans =0
        last=nums[0][1]
        for s, e in nums[1:]:
            if last>s:
                ans+=1
            else:
                last=e
        return ans 

        