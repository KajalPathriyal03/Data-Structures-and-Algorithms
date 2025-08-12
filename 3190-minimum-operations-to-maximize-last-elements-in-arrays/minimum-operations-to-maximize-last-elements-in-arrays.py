class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        e1, e2=nums1[n-1], nums2[n-1]
        dp1=0
        dp2=0
        maxi=max(e1, e2)
        mini=min(e1, e2)
        for i in range(n):
            a, b=nums1[i], nums2[i]
            if max(a, b)>maxi or min(a, b)>mini: return -1
            if a > e1 or b>e2:
                dp1+=1
            if a > e2 or b > e1:
                dp2+=1

        return min(dp1, dp2)
        