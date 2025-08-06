class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r=0, 0
        while l<m and r<n:
            print(nums1, nums2, l, r)
            nums2.sort()
            if nums1[l]>nums2[r]:
                nums1[l], nums2[r]=nums2[r], nums1[l]
                l+=1
            elif nums1[l]<nums2[r]:
                l+=1
            elif l>0 and nums1[l]==0 and nums2[r]>nums1[l]:
                nums1[l]=nums2[r]
                r+=1
            else:
                l+=1
        if nums2:
            nums2.sort()
            while r<n:
                nums1[l]=nums2[r]
                l+=1
                r+=1

        # print(nums1)

        