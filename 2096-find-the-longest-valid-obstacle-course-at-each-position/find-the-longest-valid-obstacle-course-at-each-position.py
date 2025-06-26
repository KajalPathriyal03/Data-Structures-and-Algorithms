class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        dp=[10**8 for _ in range(n+1)]

        for ele in nums:

            index=bisect.bisect(dp, ele)
            res.append(index+1)
            dp[index]=ele
            # print(index, res, dp[index])

        return res
        