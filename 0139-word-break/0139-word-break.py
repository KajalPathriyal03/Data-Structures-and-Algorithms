class Solution:
    # choices 
    # 1. start new word from current index 
    # 2. continue a word with current index 
    def rec(self, ind, s, st):
        if ind >= len(s): return True 
        if s in st: return True 
        if ind in self.dp:
            return self.dp[ind]
        for i in range(1, len(s)):
            substring=s[ind:ind+i]
            if substring in st and self.rec(ind+i, s, st):
                return True 
        self.dp[ind]= False
        return self.dp[ind]
                                                                                       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp={}
        st=set(wordDict)
        return self.rec(0, s, st)

        