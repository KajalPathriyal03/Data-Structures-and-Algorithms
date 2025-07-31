class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word)
        for i in range(1, n+1):
            d=i*k
            if d>=n:
                return i
            flag=True

            for j in range(d, n):
                if word[j]!=word[j-d]:
                    flag=False
                    break
            if flag:
                return i
        return 0
        