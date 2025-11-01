class Solution:
    def solve(self, i, s):
        # print(s[i], s[len(s)-i-1])
        if i>=len(s)//2:
            return True 

        if s[i]!=s[len(s)-i-1]: return False 
        return self.solve(i+1, s)
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s="".join(e for e in s if e.isalnum())
        return self.solve(0, s)
        