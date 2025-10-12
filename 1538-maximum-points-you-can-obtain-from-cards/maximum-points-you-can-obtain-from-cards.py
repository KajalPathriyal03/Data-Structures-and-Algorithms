class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        leftSum=sum(nums[:k])
        rightSum=0
        ans=leftSum+rightSum
        l=k-1
        r=n-1
        while l>=0 and r>=0:
            leftSum-=nums[l]
            l-=1
            rightSum+=nums[r]
            r-=1
            ans=max(ans, leftSum+rightSum)
        return ans 
        