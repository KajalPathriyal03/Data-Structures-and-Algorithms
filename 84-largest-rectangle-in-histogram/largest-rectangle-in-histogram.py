class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        ans=0
        st=[]
        for i in range(len(nums)+1):
            while st and (i==len(nums) or nums[st[-1]]>=nums[i]):
                height=nums[st.pop()]
                wt =0
                if not st:
                    wt=i
                else:
                    wt=i-st[-1]-1
                # l=prev+1
                # r=i-1
                ans=max(ans, height*wt)
            st.append(i)
        return ans 
            
        