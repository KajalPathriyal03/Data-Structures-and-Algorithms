class Solution:
    def findClosestElements(self, nums, k, x):
        h = bisect.bisect_left(nums, x)
        l = h - 1
        print(nums,h, l)
        while k > 0:
            if l < 0:
                h += 1
            elif h >= len(nums) or x - nums[l] <= nums[h] - x:
                l -= 1
            else:
                h += 1
            k -= 1
        return nums[l + 1:h]
        