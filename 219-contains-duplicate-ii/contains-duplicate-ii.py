class Solution:
    def binarySearch(self, nums, k):
        mini=float('inf')

        for i in range(len(nums)):
            if i==0:
                continue 

            mini=min(mini, nums[i]-nums[i-1])
        return mini<=k


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=defaultdict(list)

        for i, ele in enumerate(nums):
            mp[ele].append(i)

        # 1. treat the values of map as an array and find two indices where the abs difference is <= k
        ans=False
        for key, val in mp.items():
            if len(val)>1:
                ans=self.binarySearch(val, k)
        
        return ans


        
        