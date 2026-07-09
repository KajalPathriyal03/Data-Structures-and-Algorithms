class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False 
        cnt1 = Counter(s)
        cnt2=Counter(t)
        for k, v in cnt1.items():
            if k not in cnt2:
                return False 
            if cnt2[k] != v:
                return False 
        return True 
        