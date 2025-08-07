class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        l, r=0, n-1
        l_max, r_max, total=0, 0,0
        while l<=r:
            if nums[l]<=nums[r]:
                l_max=max(l_max, nums[l])
                if l_max>nums[l]:
                    total+=(l_max-nums[l])
                l+=1
            elif nums[l]>nums[r]:
                r_max=max(r_max, nums[r])
                if r_max>nums[r]:
                    total+=(r_max-nums[r])
                r-=1
        return total