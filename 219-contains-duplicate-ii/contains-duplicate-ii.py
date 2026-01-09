class Solution:
    def diff(self, nums):
        diffBetween=[]
        for i in range(1, len(nums)):
            diffBetween.append(nums[i]-nums[i-1])
        return min(diffBetween)

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=defaultdict(list)
        for i, ele in enumerate(nums):
            mp[ele].append(i)
        for key, val in mp.items():
            if len(mp[key])>1:
                if self.diff(mp[key])<=k:
                    return True 
        return False
        