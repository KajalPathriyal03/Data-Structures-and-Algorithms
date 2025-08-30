class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=bisect.bisect_left(nums, target)
        return ans
        