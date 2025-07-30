from typing import List
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def buildLps(pattern):
            m=len(pattern)
            lps=[0 for _ in range(m)]
            length=0
            i=1
            while i<m:
                if pattern[i]==pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
    
        def kmpSearch(text, pattern):
            ans=0
            n=len(text)
            m=len(pattern)
            lps=buildLps(pattern)
            i=j=0
            while i<n:
                if pattern[j]==text[i]:
                    i+=1
                    j+=1
                if j==m:
                    ans+=1
                    j=lps[j-1]
                elif i<n and pattern[j]!=text[i]:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
            return ans 
        dic={-1: "a", 0: "b", 1: "c"}
        def cvtToStr(arr):
            st=""
            n=len(arr)
            for i in range(n-1):
                if arr[i]<arr[i+1]:
                    st+=dic[1]
                elif arr[i]==arr[i+1]:
                    st+=dic[0]
                else:
                    st+=dic[-1]
            return st
        
        s=cvtToStr(nums)
        patt="".join(dic[ch] for ch in pattern)
        print(s, patt)
        res=kmpSearch(s, patt)
        return res
            
                
            
                
        