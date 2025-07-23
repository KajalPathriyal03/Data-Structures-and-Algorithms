class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n=len(nums)
        st=[]
        st.append((nums[n-1], 0))
        for i in range(n-2, -1, -1):
            tmp=0
            while st and (st[-1][0])<nums[i]:
                num, cnt=st.pop()
                tmp=max(cnt, 1+tmp)
            st.append((nums[i], tmp))
            # print(st)

        ans=0
        while st:
            ele, top=st.pop()
            ans=max(ans, top)
        return ans 



        