class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            
            if s[i].isalpha() or s[i].isdigit():
                arr.append(s[i].lower())
        for i in range(len(arr)//2):
            if arr[i]!=arr[len(arr)-i-1]:
                return False
        return True 
        
        