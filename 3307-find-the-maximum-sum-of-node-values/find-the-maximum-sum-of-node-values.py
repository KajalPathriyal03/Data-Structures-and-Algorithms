class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        cnt=0
        n=len(nums)
        mini=float('inf')
        sm=0
        for i in range(n):
            if nums[i]^k>nums[i]:
                sm+=nums[i]^k
                cnt+=1
            else:
                sm+=nums[i]
            mini=min(mini, abs(nums[i]-(nums[i]^k)))
        if cnt%2==1:
            sm-=mini
            return sm
        return sm
