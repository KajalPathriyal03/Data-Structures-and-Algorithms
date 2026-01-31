class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, r=0, 0
        n, m=len(nums1), len(nums2)
        median=(n+m)//2
        i=0
        first, sec=-1, -1
        
        while l<n and r<m:
            if nums1[l]>nums2[r]:
                if i==median-1:
                    first=nums2[r]
                if i==median:
                    sec=nums2[r]
                r+=1
            else:
                if i==median-1:
                    first=nums1[l]
                if i==median:
                    sec=nums1[l]
                l+=1    
            i+=1

        while l<n:
            if i==median-1:
                first=nums1[l]
            if i==median:
                sec=nums1[l]
            l+=1
            i+=1
        while r<m:
            if i==median-1:
                first=nums2[r]
            if i==median:
                sec=nums2[r]
            r+=1
            i+=1
        
        if (n+m) & 1:
            return float(sec)
        return (first+sec)/2

        