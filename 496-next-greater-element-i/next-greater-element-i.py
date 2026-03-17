class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        st=[]
        ans=[-1 for _ in range(len(nums2))]

        for i in range(len(nums2)-1, -1, -1):
            while st and nums2[st[-1]]<=nums2[i]:
                st.pop()

            if st:
                ans[i]=st[-1]
            
            st.append(i)
        mp={}

        for i in range(len(nums2)):
            if ans[i]==-1:
                mp[nums2[i]]=-1
            else:
                mp[nums2[i]]=nums2[ans[i]]

        res=[]
        for ele in nums1:
            if ele in mp:
                res.append(mp[ele])
            else:
                res.append(mp[ele])
        return res

        