class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i, ele in enumerate(nums):
            mp[ele]=i
        for i in range(len(nums)):
            b=target-nums[i]
            if b in mp:
                if i != mp[b]:
                    return [i, mp[b]]
                    break
        return []

