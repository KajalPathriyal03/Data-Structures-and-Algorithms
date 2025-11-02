class Solution:
    def rec(self, i, nums, res):
        if i>=len(nums):
            self.ans.append(res.copy())
            return
        res.append(nums[i])
        self.rec(i+1, nums, res)
        res.pop()
        self.rec(i+1, nums, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        res=[]
        self.rec(0, nums, res)
        return self.ans

        