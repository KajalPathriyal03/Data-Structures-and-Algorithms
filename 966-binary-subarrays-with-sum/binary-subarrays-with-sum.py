class Solution:
    def solve(self, k):
        if k<0:
            return 0
        n=len(self.nums)
        ans=0
        l, r=0,0
        sm=0
        while r<n:
            sm+=self.nums[r]
            while sm>k:
                sm-=self.nums[l]
                l+=1
            ans+=(r-l+1)
            r+=1
        return ans 

    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        self.nums=nums
        ans=self.solve(k)-self.solve(k-1)
        return ans 