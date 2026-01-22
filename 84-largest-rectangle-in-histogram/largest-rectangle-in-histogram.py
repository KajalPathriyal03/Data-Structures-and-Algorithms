class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        left_small=[-1 for _ in range(len(nums))]
        right_small=[len(nums) for _ in range(len(nums))]
        stack=[]
        stack.append(0)
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                left_small[i]=stack[-1]
            stack.append(i)
        stack=[]
        stack.append(len(nums)-1)
        for i in range(len(nums)-2,-1, -1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                right_small[i]=stack[-1]
            stack.append(i)
        ans=-1
        for i in range(len(nums)):
            distance=right_small[i]-left_small[i]-1
            ans=max(ans, distance*nums[i])
        return ans 
