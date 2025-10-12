class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        l, r=0, 0
        maxFreq=0
        mp=defaultdict(int)
        while r<n:
            mp[s[r]]+=1
            maxFreq=max(maxFreq, mp[s[r]])
            # changes=(r-l+1)-maxFreq
            while (r-l+1)-maxFreq>k:
                print(l)
                mp[s[l]]-=1
                maxFreq=0
                if mp[s[l]]==0:
                    del mp[s[l]]
                for ele, val in mp.items():
                    maxFreq=max(maxFreq, val)
                l+=1
            # if (r-l+1)-maxFreq<=k:
            ans=max(ans, r-l+1)
            # print(l, r, ans)
            r+=1
        return ans 







        