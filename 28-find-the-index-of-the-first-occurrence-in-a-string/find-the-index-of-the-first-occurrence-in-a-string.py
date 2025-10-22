class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # example: ssad, sad
        
        n, m=len(haystack), len(needle)
        if n<m: return -1
        for i in range(n-m+1):
            for j in range(m):
                print(i, j)
                if i+j<n and haystack[i+j]!=needle[j]:
                    break
                if j==m-1:
                    return i

        return -1
