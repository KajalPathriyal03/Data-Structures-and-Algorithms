class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1 for _ in range(len(nums))]
        suf=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i==0:
                pref[i]=nums[i]
            else:
                pref[i]=nums[i]*pref[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                suf[i]=nums[i]
            else:
                suf[i]=nums[i]*suf[i+1]
        ans=[1 for _ in range(len(nums))]
        ans[0]=suf[1]
        ans[len(nums)-1]=pref[len(nums)-2]
        for i in range(1, len(nums)-1):
            ans[i]=pref[i-1]*suf[i+1]
        return ans 

