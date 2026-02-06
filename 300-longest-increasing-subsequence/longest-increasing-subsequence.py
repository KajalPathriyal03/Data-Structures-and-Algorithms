class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            ind=bisect.bisect_left(ans, nums[i])
            if ind==len(ans):
                ans.append(nums[i])
            
            else:
                ans[ind]=nums[i]

        return len(ans)
        