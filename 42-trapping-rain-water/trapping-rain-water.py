class Solution:
    def trap(self, nums: List[int]) -> int:
        pref, suf=[0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i==0:
                pref[i]=nums[i]
                suf[len(nums)-i-1]=nums[len(nums)-i-1]
            else:
                pref[i]=max(pref[i-1], nums[i])
                suf[len(nums)-i-1] = max(suf[len(nums)-i], nums[len(nums)-i-1]) 
        ans=0
        for i in range(1, len(nums)-1):
            left_max=pref[i-1]
            right_max=suf[i+1]
            if min(left_max, right_max)-nums[i]>0:
                ans+=min(left_max, right_max)-nums[i]
        return ans 
                    
        