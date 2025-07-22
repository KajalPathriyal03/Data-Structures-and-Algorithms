class Solution:
    def maximumWhiteTiles(self, nums: List[List[int]], ln: int) -> int:
        n=len(nums)
        nums.sort()
        pref=[0 for _ in range(n+1)]
        lastInd=[0 for _ in range(n)]
        for i in range(1, n+1):
            pref[i]=pref[i-1]+(nums[i-1][1]-nums[i-1][0]+1)
            lastInd[i-1]=nums[i-1][1]
        print(pref, lastInd)
        ans=0
        for i in range(n):
            l=nums[i][0]
            cend=l+ln-1
            ind=bisect.bisect_right(lastInd, cend)
            print(ind, cend)
            cnt=pref[ind]
            if ind<n and nums[ind][0]<=cend:
                cnt+=cend-nums[ind][0]+1
            if i>0:
                cnt-=pref[i]
            ans=max(ans, cnt)
        return ans 


