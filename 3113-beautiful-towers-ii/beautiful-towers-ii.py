class Solution:
    def maximumSumOfHeights(self, nums: List[int]) -> int:
        n=len(nums)
        left_smaller=[-1 for _ in range(n)]
        stack=[]
        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                left_smaller[i]=-1
            else:
                left_smaller[i]=stack[-1]
            stack.append(i)
        st=[]
        right_smaller=[n for _ in range(n)]
        for i in range(n-1, -1, -1):
            while st and nums[i]<=nums[st[-1]]:
                st.pop()
            if not st:
                right_smaller[i]=n
            else:
                right_smaller[i]=st[-1]
            st.append(i)
        print(left_smaller, right_smaller)

        left_peak_sum=[0 for _ in range(n)]
        right_peak_sum=[0 for _ in range(n)]

        for i in range(n):
            left_peak_sum[i]=nums[i]
            if i==0: continue
            if nums[i]>=nums[i-1]:
                left_peak_sum[i]+=left_peak_sum[i-1]
            else:
                if left_smaller[i]<0:
                    left_peak_sum[i]+=(i-left_smaller[i]-1)*nums[i]
                else:
                    left_peak_sum[i]+=(i-left_smaller[i]-1)*nums[i]+(left_peak_sum[left_smaller[i]])

        for i in range(n-1, -1, -1):
            right_peak_sum[i]=nums[i]
            if i==n-1: continue
            if nums[i]>=nums[i+1]:
                right_peak_sum[i]+=right_peak_sum[i+1]
            else:
                if right_smaller[i]==n:
                    right_peak_sum[i]+=(right_smaller[i]-i-1)*nums[i]
                else:
                    right_peak_sum[i]+=(right_smaller[i]-i-1)*nums[i]+(right_peak_sum[right_smaller[i]])
        # print(left_peak_sum, right_peak_sum)
        maxi=0
        for i in range(n):
            cur=right_peak_sum[i]+left_peak_sum[i]-nums[i]
            maxi=max(maxi, cur)
            # print(i, maxi)
        return maxi
        






        