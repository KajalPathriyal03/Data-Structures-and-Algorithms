class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        n, m=len(A), len(B)
        right=defaultdict(int)
        st=[]
        for i in range(m-1, -1, -1):
            while st and B[st[-1]]<=B[i]:
                st.pop()
            if len(st)==0:
                right[B[i]]=-1
            else:
                right[B[i]]=B[st[-1]]
            st.append(i)
        ans=[]
        for ele in A:
            if ele in right:
                ans.append(right[ele])
            else:
                ans.append(-1)
        return ans 

        