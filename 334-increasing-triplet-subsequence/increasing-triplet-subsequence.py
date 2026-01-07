class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left_small=[-1 for _ in range(len(nums))]
        st=[]
        st.append(0)
        for i in range(1, len(nums)):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:
                left_small[i]=st[-1]
            st.append(i)
        right_large=[-1 for _ in range(len(nums))]
        st=[]
        st.append(len(nums)-1)
        for i in range(len(nums)-2, -1, -1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if st:
                right_large[i]=st[-1]
            st.append(i)
            if left_small[i]!=-1 and right_large[i]!=-1:
                return True 


        return False 



