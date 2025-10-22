class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        n=len(nums)
        st=[]
        ans=[]
        for i in range(n):
            while st and nums[i]<0<st[-1]:
                if -nums[i]>st[-1]:
                    st.pop()
                    continue
                elif -nums[i]==st[-1]:
                    st.pop()
                break
            else:
                st.append(nums[i])
        return st






        