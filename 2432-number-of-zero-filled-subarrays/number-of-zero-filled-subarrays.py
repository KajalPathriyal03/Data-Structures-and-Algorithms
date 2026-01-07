class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l, r=0, 0
        cnt=0
        while r<len(nums):
            if nums[r]==0:
                l=r
                while r<len(nums) and nums[r]==0:
                        r+=1
                sz=r-l+1
                cnt+=sz-1
                for i in range(1, sz-1):
                    cnt+=i
            else:
                l=r+1
            r+=1
        return cnt

        