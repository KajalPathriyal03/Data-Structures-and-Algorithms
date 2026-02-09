class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cp=1
        mp=max(nums)
        for ele in nums:
            cp*=ele
            if cp>mp:
                mp=cp
            if cp==0:
                cp=1
        cp=1
        for i in range(len(nums)-1,-1, -1):
            ele=nums[i]
            cp*=ele
            if cp>mp:
                mp=cp
            if cp==0:
                cp=1


        return mp
        