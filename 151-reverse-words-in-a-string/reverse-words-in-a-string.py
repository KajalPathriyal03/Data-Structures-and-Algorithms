class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        l, r=0, 0
        while l<len(s):
            if s[l]!=" ":
                r=l
                while r<len(s):
                    if s[r]==" ":
                        break
                    r+=1
                arr.append(s[l:r])
                l=r
            l+=1

        s=" ".join(arr)

        ans=""
        l, r=len(s)-1, len(s)-1
        while l>=0:
            if s[l]==" ":
                ans+=s[l+1:r+1]
                ans+=" "
                r=l-1
            l-=1
        ans+=s[l+1:r+1]
        return ans 

        