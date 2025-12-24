class Solution:
    def rec(self, i, j, word1, word2):
        if i>=len(word1):
            return len(word2)-j
        if j>=len(word2):
            return len(word1)-i
        if (i,j ) in self.dp:
            return self.dp[(i, j)]
        ans=0
        if word1[i]==word2[j]:
            ans=self.rec(i+1,j+1, word1, word2)
        else:
            insert=self.rec(i, j+1, word1, word2)
            delete=self.rec(i+1, j, word1, word2)
            replace=self.rec(i+1, j+1, word1, word2)
            ans=1+min(insert, delete, replace)
        self.dp[(i, j)]= ans 
        return self.dp[(i, j)]

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp={}
        ans=self.rec(0,0, word1,word2)
        return ans 
        