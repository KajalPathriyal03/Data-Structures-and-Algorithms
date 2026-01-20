class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxi=0
        mp=defaultdict(int)
        sm=0

        for i in range(k):
            sm+=nums[i]
            mp[nums[i]]+=1
    
        r=k
        while r<len(nums):
            if len(mp)==k:
                maxi=max(maxi, sm)
            mp[nums[r]]+=1
            sm+=nums[r]
            mp[nums[r-k]]-=1
            sm-=nums[r-k]
            if mp[nums[r-k]]==0:
                del mp[nums[r-k]]
            r+=1
        if len(mp)==k:
                maxi=max(maxi, sm)
        return maxi
        