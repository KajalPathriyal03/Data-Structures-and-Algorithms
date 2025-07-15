class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n=10**5
        cnt=[0 for _ in range(n+1)]
        maxi=-n
        for i in range(len(nums1)):
            maxi=max(maxi, abs(nums1[i]-nums2[i]))
            cnt[abs(nums1[i]-nums2[i])]+=1
        
        
        ops=k1+k2
        for dif in range(maxi, 0, -1):
            if cnt[dif]==0: continue

            if ops>=cnt[dif]:
                cnt[dif-1]+=cnt[dif]
                ops-=cnt[dif]
                cnt[dif]=0
            else:
                cnt[dif-1]+=ops
                cnt[dif]-=ops
                ops=0
                break
        ans=0
        for i in range(1, n+1):
            if cnt[i]>0:
                ans+=cnt[i]*(i**2)
        return ans
        



