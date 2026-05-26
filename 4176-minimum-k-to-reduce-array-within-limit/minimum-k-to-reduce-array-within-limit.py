class Solution:
    def binarySearch(self, k, nums):
        ops=0
        for i in range(len(nums)):
            while nums[i]>0:
                nums[i]-=k
                ops+=1

        return ops
    def minimumK(self, nums: List[int]) -> int:
        arr=nums
        ans=max(nums)
        l, r=1, max(max(nums), len(nums))
        while l<=r:
            mid=(l+r)//2
            ops=0
            for ele in nums:
                ops+=(ele+mid-1)//mid
            if ops<=mid*mid:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans 
        
        
        