class Solution:
    def dfs(self, i,j, w1, w2):
        if j==len(w2):
            return len(w1)-i
        if i>=len(w1):
            return len(w2)-j
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        ans = float('inf')
        if w1[i]==w2[j]:
            ans=self.dfs(i+1, j+1, w1, w2)
        else:
            o1=self.dfs(i+1, j+1, w1, w2)
            o2=self.dfs(i+1, j, w1, w2)
            o3=self.dfs(i, j+1, w1, w2)
            ans = min(ans, 1+min(o1, o2, o3))
        self.dp[(i, j)]= ans 
        return self.dp[(i, j)]

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp={}
        return  self. dfs(0, 0, word1, word2)

        