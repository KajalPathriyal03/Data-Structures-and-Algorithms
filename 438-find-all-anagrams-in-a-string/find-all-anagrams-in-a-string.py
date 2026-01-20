class Solution:
    def anagram(self, s):
        nums=list(s)
        nums.sort()
        return "".join(nums)
        

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        target=self.anagram(p)
        ans=[]
        k=len(p)
        r=k
        while r<=len(s):
            st=self.anagram(s[r-k:r])
            if st==target:
                ans.append(r-k)
            r+=1
        return ans 
        
        
        
        