class Solution:  
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): 
            return []
        mp=defaultdict(int)
        dp=defaultdict(int)

        for ele in p:
            mp[ele]+=1

        ans=[]
        k=len(p)

        for i in range(k):
            dp[s[i]]+=1

        r=k
        while r<len(s):
            if mp==dp:
                ans.append(r-k)
            dp[s[r]]+=1
            dp[s[r-k]]-=1
            if dp[s[r-k]]==0:
                del dp[s[r-k]]
            r+=1
        if mp==dp:
            ans.append(r-k)

        return ans 
        
        
        
        