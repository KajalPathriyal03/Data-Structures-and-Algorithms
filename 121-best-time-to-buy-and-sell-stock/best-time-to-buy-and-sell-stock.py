class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[len(prices)-1]
        profit=0
        for i in range(len(prices)-2, -1, -1):
            ele=prices[i]
            profit=max(profit, buy-ele)
            buy=max(buy, ele)
        return profit
        