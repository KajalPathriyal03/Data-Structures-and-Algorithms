''' as it depends only on last two points so we dont need any dp here only two variables are enogh'''
class Solution:
    def rec(self, ind, cost, cur_cost):
        if ind >= len(cost):
            self.mini=min(self.mini, cur_cost)
            return 
        self.rec(ind+1, cost, cur_cost+cost[ind])
        self.rec(ind+2, cost, cur_cost+cost[ind])
        

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        self.dp={} # till ith point what is the minimum cost 
        f, s=cost[0],cost[1]
        if n==0: return 0
        if n==1: return f
        if n==2: return min(f, s)

        for i in range(2, n):
            cur=cost[i]+min(f, s)
            f=s
            s=cur 
        return min(f, s)