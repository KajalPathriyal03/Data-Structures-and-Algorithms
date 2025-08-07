class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        pref_max=[0 for _ in range(n)]
        suf_max=[0 for _ in range(n)]
        pref_max[0]=nums[0]
        suf_max[n-1]=nums[n-1]
        for i in range(1, n):
            pref_max[i]=max(pref_max[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suf_max[i]=max(suf_max[i+1], nums[i])
        
        ans=0
        for i in range(1, n-1):
            if nums[i]<pref_max[i-1] and nums[i]<suf_max[i+1]:
                ans+=min(pref_max[i-1], suf_max[i+1])-nums[i]
        return ans