class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0 for _ in range(len(temperatures))]

        st=[]
        for i in range(len(temperatures)-1, -1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if st:
                ans[i]=st[-1]-i

            st.append(i)

        return ans 
        