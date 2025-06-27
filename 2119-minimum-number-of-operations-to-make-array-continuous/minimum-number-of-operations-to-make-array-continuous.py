class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums=sorted(set(nums))
        res=n
        #sliding window
        r=0
        for l in range(len(nums)):
            while r<len(nums) and nums[r]<nums[l]+n:
                r+=1
            window=r-l
            res=min(res, n-window)
        return res
