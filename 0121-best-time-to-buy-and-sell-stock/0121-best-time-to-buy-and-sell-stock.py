class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy=nums[len(nums)-1]
        maxi=0
        for i in range(len(nums)-2, -1, -1):
            maxi=max(maxi, buy-nums[i])
            buy=max(buy, nums[i])
        return maxi

        