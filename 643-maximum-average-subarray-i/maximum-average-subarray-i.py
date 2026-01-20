class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pref=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i==0:
                pref[i]=nums[i]
            else:
                pref[i]=pref[i-1]+nums[i]
        l, r=0,k-1
        maxi=float('-inf')
        while r<len(nums):
            sm=0
            if l==0:
                sm=pref[r]
            else:
                sm=pref[r]-pref[l-1]
            maxi=max(maxi, sm/k)
            r+=1
            l+=1
        return maxi
            

        