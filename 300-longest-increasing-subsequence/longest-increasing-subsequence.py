class Solution:
    def lower_bound(self, nums, target):
        ans=len(nums)
        l, r=0, len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans 
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            ind=self.lower_bound(ans, nums[i])
            if ind==len(ans):
                ans.append(nums[i])
            
            else:
                ans[ind]=nums[i]

        return len(ans)
        