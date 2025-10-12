class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp=defaultdict(int)
        ans=0
        n=len(s)
        l, r=0, 0
        while r<n:
            mp[s[r]]=r
            if len(mp)==3:
                mini=min(mp['a'], mp['b'], mp['c'])
                ans+=mini+1
                # l=mini+1
            r+=1
        return ans 
                

        