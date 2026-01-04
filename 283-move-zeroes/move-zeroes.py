class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r=0, len(nums)-1
        i=0
        while l<=r:
            if nums[i]!=0:
                nums[l]=nums[i]
                l+=1
            else:
                r-=1
            i+=1
        r=r+1
        while r<len(nums):
            nums[r]=0
            r+=1

        return nums 
        