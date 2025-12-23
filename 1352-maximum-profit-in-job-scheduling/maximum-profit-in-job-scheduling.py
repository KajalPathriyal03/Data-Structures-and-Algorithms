class Solution:
    def binarySearch(self, l, target, nums):
        r=len(nums)-1
        ans=len(nums)+1
        while l<=r:
            mid=(l+r)//2
            if nums[mid][0]>=target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans 

    def rec(self, start, nums):
        if start>=len(nums): return 0
        if start in self.dp:
            return self.dp[start]
            
        nextInd=self.binarySearch(start+1, nums[start][1],  nums)

        not_take=self.rec(start+1, nums)
        take = nums[start][2]+self.rec(nextInd, nums)
        self.dp[start]= max(not_take, take)
        return self.dp[start]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.dp={}
        lst=[list(a) for a in (zip(startTime, endTime, profit))]
        lst.sort()

        ans=self.rec(0, lst)
        return ans 

        