class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0 for _ in range(n)]
        stack=[]
        for i in range(n-1, -1, -1):
            ele=nums[i]
            while stack and nums[stack[-1]]<=ele:
                stack.pop()
                ans[i]+=1
            if stack:
                ans[i]+=1
            stack.append(i)
        return ans 
        