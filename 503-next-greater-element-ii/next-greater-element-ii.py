class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        ans=[-1 for _ in range(len(nums))]

        for i in range(2*len(nums)):
            ind=i%len(nums)
            while st and nums[st[-1]]<nums[ind]:
                ans[st[-1]]=nums[ind]
                st.pop()
            st.append(ind)
        return ans 




        