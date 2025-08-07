class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        left_small=[-1 for _ in range(len(nums))]
        right_small=[-1 for _ in range(len(nums))]
        n=len(nums)
        st=[]
        maxi=0
        for i in range(n+1):
            while st  and (i==n or nums[st[-1]]>=nums[i]):
                h=nums[st[-1]]
                st.pop()
                w=0
                if not st:
                    w=i
                else:
                    w=i-st[-1]-1
                maxi=max(maxi, h*w)
            st.append(i)
        return maxi