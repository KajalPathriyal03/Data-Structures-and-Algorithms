class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        l, r=0, 0
        ans=0
        while r<len(s):
            ch=s[r]
            if ch not in mp:
                mp[ch]=r
            else:
                if mp[ch]+1>l:
                    l=mp[ch]+1
                mp[ch]=r
            ans=max(ans, r-l+1)
            r+=1
        return ans 
            
            
        