class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        # stack.append()
        for i in range(len(s)):
            if stack and stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        ans=""
        while stack:
            ans=stack.pop()+ans
        return ans 

