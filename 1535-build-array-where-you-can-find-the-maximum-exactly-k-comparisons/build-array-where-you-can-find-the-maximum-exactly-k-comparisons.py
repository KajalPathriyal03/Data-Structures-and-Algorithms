class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        dp={}
        def solve(ind, search_cost, max_so_far):
            if ind==n:
                if search_cost==k:
                    return 1
                else:
                    return 0
            if (ind, search_cost, max_so_far) in dp:
                return dp[(ind, search_cost, max_so_far)]
            res=0
            for i in range(1, m+1):
                if i>max_so_far:
                    res=(res+solve(ind+1, search_cost+1, i))%mod
                else:
                    res=(res+solve(ind+1, search_cost, max_so_far))%mod
            dp[(ind, search_cost, max_so_far)]= res%mod
            return dp[(ind, search_cost, max_so_far)]

        return solve(0, 0, -1)
        