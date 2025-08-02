class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        
        st1=set(nums1)
        st2, common=set(), set()
        for ele in nums2:
            st2.add(ele)
            if ele in st1:
                common.add(ele)
        n1, n2, s=len(st1), len(st2), len(common)
        ans=min(n, min(n1-s, n//2)+min(n2-s, n//2)+s)
        return ans 
        