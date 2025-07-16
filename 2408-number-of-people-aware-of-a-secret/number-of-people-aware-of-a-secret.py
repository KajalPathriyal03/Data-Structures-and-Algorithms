class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod=10**9+7
        dp=[0]*2005
        dp[1]=1
        for i in range(1, n+1):
            for j in range(i+delay, i+forget):
                dp[j]=(dp[j]+dp[i])%mod
        ans=0
        for i in range(max(1, n-forget+1), n+1):
            ans+=dp[i]%mod
        return ans%mod
        
                
                



         