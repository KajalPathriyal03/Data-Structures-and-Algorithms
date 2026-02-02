class Solution:
    def backtrack(self, ind, nums, ans):
        self.res.append(ans.copy())
        for i in range(ind, len(nums)):
            ans.append(nums[i])
            self.backtrack(i+1, nums, ans)
            ans.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        ans=[]
        nums.sort()
        self.backtrack(0, nums, ans)
        return self.res

        