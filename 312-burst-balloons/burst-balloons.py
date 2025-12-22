class Solution:
    def rec(self, i, j, nums):
        if i>j: return 0
        if (i, j)in self.dp:
            return self.dp[(i, j)]
        maxi=float('-inf')
        for ind in range(i, j+1):
            cost=nums[ind]*nums[i-1]*nums[j+1]+self.rec(i,ind-1, nums)+self.rec(ind+1, j,nums)
            maxi=max(maxi, cost)
        self.dp[(i, j)]=maxi
        return self.dp[(i, j)]

    def maxCoins(self, nums: List[int]) -> int:
        self.dp={}
        nums.insert(0, 1)
        nums.append(1)
        ans=self.rec(1, len(nums)-2, nums)
        return ans 
        