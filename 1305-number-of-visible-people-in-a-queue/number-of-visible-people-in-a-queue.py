class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0 for _ in range(n)]
        stack=[]
        for i, ele in enumerate(nums):
            while stack and nums[stack[-1]]<=ele:
                top=stack.pop()
                ans[top]+=1
            if stack:
                ans[stack[-1]]+=1
            stack.append(i)
        return ans 
        