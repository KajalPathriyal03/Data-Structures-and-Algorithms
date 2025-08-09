class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n=len(nums)
        left_small=[-1 for _ in range(n)]
        right_small=[-1 for _ in range(n)]
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                left_small[i]=0
            else:
                left_small[i]=st[-1]+1
            st.append(i)
        st=[]
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                right_small[i]=n-1
            else:
                right_small[i]=st[-1]-1
            st.append(i)
        maxi=0
        for i in range(n):
            maxi=max(maxi, nums[i]*(right_small[i]-left_small[i]+1))
        return maxi



                                                                                                                                                                                                                    