class Solution:
    def rec(self, ind1, ind2, text1, text2):
        if ind1>=len(text1) or ind2>=len(text2):
            return 0
        if (ind1, ind2) in self.dp:
            return self.dp[(ind1, ind2)]
        ans=0
        if text1[ind1]==text2[ind2]:
            # self.s+=text1[ind1]
            ans=1+self.rec(ind1+1, ind2+1, text1, text2)

        else:
            one=self.rec(ind1+1, ind2, text1, text2)
            two=self.rec(ind1,ind2+1, text1, text2)
            ans=max(one, two)

        self.dp[(ind1, ind2)]= ans 
        return self.dp[(ind1, ind2)]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp={}
        self.s=""
        ans =self.rec(0, 0, text1, text2)
        return ans 
        