class Solution:
    def countTexts(self, keys: str) -> int:
        mod=10**9+7
        n=len(keys)
        @cache
        def dfs(ind,  continous):
            if ind>=n:
                return 1
            not_take=dfs(ind+1, 1)
            take=0
            if ind+1<n and keys[ind+1]==keys[ind]:
                if keys[ind] in "79":
                    cnt=4
                else:
                    cnt=3
                if continous<cnt:
                    take+=dfs(ind+1, continous+1)
            ans=take+not_take
            return ans%mod
        return dfs(0, 1)%mod

        