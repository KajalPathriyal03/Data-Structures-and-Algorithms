class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split()
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

        