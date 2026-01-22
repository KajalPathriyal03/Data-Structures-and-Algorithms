class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        mp=defaultdict(int) # latest occurence 
        l, r=0,0
        maxi=0
        while r<len(s):
            if s[r] not in mp:
                mp[s[r]]=r
            else:
                l=max(l, mp[s[r]]+1)
                mp[s[r]]=r
            maxi=max(maxi, r-l+1)
            r+=1
        return maxi


