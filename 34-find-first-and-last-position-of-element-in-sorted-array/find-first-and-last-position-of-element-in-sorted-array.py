class Solution:
    def lower_bound(self, nums, target):
        l, r=0, len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans 
    
    def upper_bound(self, nums, target):
        l, r=0, len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.lower_bound(nums, target)
        b=self.upper_bound(nums, target)
        return [a, b]
        