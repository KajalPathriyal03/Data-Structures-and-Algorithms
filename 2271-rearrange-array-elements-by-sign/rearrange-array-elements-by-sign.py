class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l, r=0, n-1
        ans=[-1 for _ in range(n)]
        even=0
        odd=n-1
        while l<n and r>=0:
            if nums[l]>0:
                ans[even]=nums[l]
                even+=2
            if nums[r]<0  :
                ans[odd]=nums[r]
                odd-=2
            r-=1
            l+=1
        return ans 

        