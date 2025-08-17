class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        pref_sum=[0 for _ in range(n+1)]
        for i in range(n):
            pref_sum[i]=pref_sum[i-1]+nums[i]

        l,r=0,0
        sm=0
        mini=float('inf')
        ans=0
        cur=nums[0]
        while r<n:
            ele=nums[r]
            cur&=ele
            # print(l, r,cur, nw)
            if cur==0:
                ans+=1
                l=r+1
                if l<n:
                    cur=nums[l]
                else:
                    break
            r+=1
        if ans==0:
            return 1
            
        return ans 









        