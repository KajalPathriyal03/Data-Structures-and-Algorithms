class Solution:
    def candy(self, nums: List[int]) -> int:
        n=len(nums)
        pref=[1 for _ in range(n)]
        suf=[1 for _ in range(n)]
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                pref[i]=1+pref[i-1]
        
        for i in range(n-2, -1, -1):
            if nums[i]>nums[i+1]:
                suf[i]=max(pref[i], suf[i+1]+1)
        ans=0
        for i in range(n):
            ans+=max(pref[i], suf[i])       
        # print(pref, suf)
        return ans