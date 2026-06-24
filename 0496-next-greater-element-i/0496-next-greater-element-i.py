class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1 for _ in range(len(nums2))]
        st=[]
        for i in range(len(nums2)-1, -1, -1):
            while st and nums2[st[-1]]<=nums2[i]:
                st.pop()
            if st:
                ans[i]=nums2[st[-1]]
            st.append(i)
        
        mp={}
        for i, ele in enumerate(nums2):
            mp[ele]=i
        res=[]
        
        for ele in nums1:
            ind=mp[ele]
            res.append(ans[ind])
        return res

