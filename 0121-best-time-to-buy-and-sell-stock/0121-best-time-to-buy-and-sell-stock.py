class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        suf=[-1 for _ in range(len(nums))]
        maxi=0
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                suf[i]=nums[i]
            if i+1<len(nums):
                maxi=max(maxi, suf[i+1]-nums[i])
                suf[i]=max(suf[i+1], nums[i])
        return maxi

        