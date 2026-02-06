class Solution:
    def rec(self, ind, coins,amount):
        if amount==0:
            return 0
        if ind>=len(coins):
            return float('inf')
        if (ind, amount) in self.dp:
            return self.dp[(ind,amount)]
        nottake=self.rec(ind+1, coins, amount)
        take=float('inf')
        if coins[ind]<=amount:
            take=1+self.rec(ind,coins, amount-coins[ind])
        self.dp[(ind,amount)] = min(take, nottake)
        return self.dp[(ind,amount)]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp={}
        ans= self.rec(0, coins, amount)
        if ans ==float('inf'):
            return -1
        return ans 
        