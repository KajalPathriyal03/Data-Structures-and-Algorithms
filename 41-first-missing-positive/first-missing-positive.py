from sortedcontainers import  SortedSet
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            ind=nums[i]-1
            if nums[i]>=1 and nums[i]<=n and nums[i] != nums[ind]:
                nums[i], nums[ind]=nums[ind], nums[i]
            else:
                i+=1

        # print(nums)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
