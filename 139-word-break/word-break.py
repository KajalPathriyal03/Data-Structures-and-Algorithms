class Solution:
    def rec(self, ind, s, st):
        if ind==len(s):
            return True 
        if s in st:
            return True 
        if ind in self.dp:
            return self.dp[ind]

        for l in range(1, len(s)+1):
            substr=s[ind:ind+l]
            # print(substr)
            if substr in st and (self.rec(ind+l, s, st)):
                return True 
        
        self.dp[ind]= False 
        return self.dp[ind]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dp={}
        return self.rec(0, s, set(wordDict))


        