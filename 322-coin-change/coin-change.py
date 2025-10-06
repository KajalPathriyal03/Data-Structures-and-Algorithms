class Solution:
    def solve(self, ind, amount):
        if ind==0:
            if amount%self.coin[ind]==0:
                return amount//self.coin[ind]
            else:
                return float('inf')
        if self.dp[ind][amount]!=-1:
            return self.dp[ind][amount]
        not_take=0+self.solve(ind-1, amount)
        take=float('inf')
        if self.coin[ind]<=amount:
            take=1+self.solve(ind, amount-self.coin[ind])
        self.dp[ind][amount]= min(not_take, take)
        return self.dp[ind][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        self.dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        self.coin=coins
        ans=self.solve(n-1, amount)
        if ans>=float('inf'):
            return -1
        return ans 
        