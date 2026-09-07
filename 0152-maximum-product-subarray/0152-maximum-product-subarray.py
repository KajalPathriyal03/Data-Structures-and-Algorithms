class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref, suf = 1, 1
        maxi=max(nums)
        for i in range(len(nums)):
            pref*=nums[i]
            suf*=nums[len(nums)-i-1]
            maxi=max(maxi, pref, suf)
            if pref==0: 
                pref=1

            if suf==0:
                suf=1
        return maxi

        