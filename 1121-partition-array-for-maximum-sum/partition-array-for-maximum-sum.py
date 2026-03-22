class Solution:
    def rec(self, i, arr, k):
        if i == len(arr):
            return 0
        if i in self.dp:
            return self.dp[i]
        curMax=curSum=0
        for j in range(i, min(i+k, len(arr))):
            curMax=max(curMax, arr[j])
            cur=curMax*(j-i+1)+self.rec(j+1, arr,k)
            curSum=max(curSum, cur)
        self.dp[i]= curSum
        return self.dp[i]
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.dp={}
        return self.rec(0, arr, k)
        