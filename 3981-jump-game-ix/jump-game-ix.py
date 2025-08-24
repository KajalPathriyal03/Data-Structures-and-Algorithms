class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        pre = [0] * n
        suff = [0] * n
        res = [0] * n

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(nums[i], pre[i - 1])

        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(nums[i], suff[i + 1])

        res[n - 1] = pre[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] = pre[i]
            if pre[i] > suff[i + 1]:
                res[i] = res[i + 1]

        return res