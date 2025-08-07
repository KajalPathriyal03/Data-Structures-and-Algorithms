class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        left_small=[-1 for _ in range(len(nums))]
        right_small=[-1 for _ in range(len(nums))]
        n=len(nums)
        st=[]
        for i in range(n):
            if not st:
                left_small[i]=0
                st.append(i)
            else:
                print(nums[st[-1]])
                if nums[i] <= nums[st[-1]]:
                    while st and nums[st[-1]]>=nums[i]:
                        st.pop()
                    if st:
                        left_small[i]=(st[-1])+1
                    else:
                        left_small[i]=0
                    st.append(i)
                elif nums[i] >= nums[st[-1]]:
                    left_small[i]=(st[-1])+1
                    st.append(i)
        st=[]
        for i in range(n-1, -1, -1):
            if not st:
                right_small[i]=n-1
                st.append(i)
            else:
                if nums[i]<=nums[st[-1]]:
                    while st and nums[st[-1]]>=nums[i]:
                        st.pop()
                    if st:
                        right_small[i]=st[-1]-1
                    else:
                        right_small[i]=n-1
                    st.append(i)
                elif nums[i] >= nums[st[-1]]:
                    right_small[i]=st[-1]-1
                    st.append(i)
        print(left_small, right_small)
        maxi=-1
        for i in range(n):
            ans=nums[i]*(right_small[i]-left_small[i]+1)
            maxi=max(maxi, ans)
        return maxi





