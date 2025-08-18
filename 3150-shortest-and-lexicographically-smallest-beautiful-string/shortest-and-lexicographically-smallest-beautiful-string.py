from sortedcontainers import SortedSet
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        cnt=0
        ans=""
        l, r=0, 0
        while r<n:
            if s[r]=="1":
                cnt+=1
            if cnt==k:
                while l<n and cnt==k:
                    tmp=s[l:r+1]
                    if not ans or len(ans)>len(tmp):
                        ans=tmp
                    elif len(ans)==len(tmp):
                        ans=min(ans, tmp)
                    if s[l]=="1":
                        cnt-=1
                    l+=1
            r+=1
        return ans 

            
                
            
                
            
        