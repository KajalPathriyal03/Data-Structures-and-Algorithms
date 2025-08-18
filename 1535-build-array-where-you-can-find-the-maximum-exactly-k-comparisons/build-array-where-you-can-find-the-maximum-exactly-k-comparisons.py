class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        @cache
        def solve(ind, search_cost, max_so_far):
            if ind==n:
                if search_cost==k:
                    return 1
                else:
                    return 0
            res=0
            for i in range(1, m+1):
                if i>max_so_far:
                    res=(res+solve(ind+1, search_cost+1, i))%mod
                else:
                    res=(res+solve(ind+1, search_cost, max_so_far))%mod
            return res%mod

        return solve(0, 0, -1)
        