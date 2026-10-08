class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=0
        o=0 
        ans =0
        for ele in s:
            if int(ele) & 1:
                o+=1
            else:
                z+=1
            
            if abs(o-z)<=1:
                ans+=1 
        return ans 
        