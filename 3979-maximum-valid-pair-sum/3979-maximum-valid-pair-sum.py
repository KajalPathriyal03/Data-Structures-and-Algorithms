class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        sufMax=[ele for ele in nums]
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1: continue
            sufMax[i]=max(sufMax[i+1], sufMax[i])

        maxi=0
        for i in range(len(nums)):
            j=i+k
            if j>=len(nums): continue
            maxi=max(maxi, nums[i]+sufMax[j])
        return maxi                
        