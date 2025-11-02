class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n=len(nums)
        left_small=[-1 for _ in range(n)]
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                left_small[i]=-1
            else:
                left_small[i]=st[-1]
            st.append(i)
        right_small=[n for _ in range(n)]
        st=[]
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                right_small[i]=n
            else:
                right_small[i]=st[-1]
            st.append(i)
        print(right_small)

        ans=0
        for i in range(n):
            l=left_small[i]+1
            r=right_small[i]-1
            ans=max(ans, nums[i]*(r-l+1))
        return ans 




        