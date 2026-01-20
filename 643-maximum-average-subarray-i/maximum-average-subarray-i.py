class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm=0
        for i in range(k):
            sm+=nums[i]
        if len(nums)==k:
            return sm/k
        l, r=1, k
        maxi=sm/k
        while r<len(nums):
            sm+=nums[r]
            sm-=nums[l-1]
            maxi=max(maxi, sm/k)
            r+=1
            l+=1
            
        return maxi

# 9 16 19 24 30 32 32 40 41 50
            

        