class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r=0, len(nums)-1
        maxi=0
        while l<r:
            b=r-l
            maxi=max(maxi, min(nums[l], nums[r])*b)
            if nums[l]<=nums[r]:
                l+=1
            elif nums[r]<nums[l]:
                r-=1
        return maxi
            
        