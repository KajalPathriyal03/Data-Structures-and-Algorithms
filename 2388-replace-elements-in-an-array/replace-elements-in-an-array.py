class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n=len(nums)
        st=defaultdict(int)
        for i, ele in enumerate(nums):
            st[ele]=i
        new=defaultdict(int)
        for ele, replace in operations:
            i=st[ele]
            # new[replace]=i
            del st[ele]
            st[replace]=i
        # print(st)
        ans=[-1 for _ in range(n) ]
        for ele, i in st.items():
            ans[i]=ele
        for i in range(n):
            if ans[i]==-1:
                ans[i]=nums[i]
        return ans
        