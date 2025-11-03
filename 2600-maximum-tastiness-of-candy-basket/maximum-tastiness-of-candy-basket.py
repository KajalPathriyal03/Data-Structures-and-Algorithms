class Solution:
    def isPossible(self, nums, mid, k):
        cnt=1
        last=nums[0]
        for i in range(len(nums)):
            if nums[i]-last>=mid:
                cnt+=1
                last=nums[i]
            if cnt>=k:
                return True 
        return False

    def maximumTastiness(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=max(nums)-min(nums)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if self.isPossible(nums,mid, k):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans 
        