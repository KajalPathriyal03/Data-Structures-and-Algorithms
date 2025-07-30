class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def lowerBound(nums, target):
            l, r=0, n-1
            ans=float('inf')
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            if ans == float('inf'):
                return -1
            return ans 
        ans1=lowerBound(nums, target)
        def upperBound(nums, target):
            l, r=0,n-1
            ans=float('inf')
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            if ans == float('inf'):
                return -1
            return ans 
        ans2=upperBound(nums, target)
        return [ans1, ans2]



            
        