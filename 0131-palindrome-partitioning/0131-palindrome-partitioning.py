class Solution:
    def isPallindrome(self, s):
        return s==s[::-1]

    def backtrack(self, i, s, ans):
        if i==len(s):
            self.res.append(ans.copy())
            return 

        for index in range(i, len(s)):
            if self.isPallindrome(s[i:index+1]):
                ans.append(s[i:index+1])
                self.backtrack(index+1, s, ans)
                ans.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        self.backtrack(0, s, [])
        return self.res
        