class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r=0, 0
        mp={}
        maxi=0
        while r<len(s):
            if s[r] in mp:
                l=max(l, mp[s[r]]+1)
            mp[s[r]]=r
            sz=r-l+1
            maxi=max(maxi, sz)
            r+=1
        return maxi
        