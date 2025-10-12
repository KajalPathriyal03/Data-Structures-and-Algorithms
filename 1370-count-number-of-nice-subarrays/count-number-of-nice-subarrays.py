class Solution:
    def solve(self, k):
        if k<0:
            return 0
        n=len(self.nums)
        ans=0
        l, r=0,0
        odd=0
        while r<n:
            if self.nums[r]%2==1:
                odd+=1
            while odd>k:
                if self.nums[l]%2==1:
                    odd-=1
                l+=1
            ans+=(r-l+1)
            r+=1
        return ans
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        self.nums=nums
        ans=self.solve(k)-self.solve(k-1)
        return ans  



