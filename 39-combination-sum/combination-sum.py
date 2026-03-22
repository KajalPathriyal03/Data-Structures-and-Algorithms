class Solution:
    def rec(self, ind, nums, target, res):
        if target==0:
            self.ans.append(res.copy())
            return 
        if ind>=len(nums):
            return 
        if nums[ind]<=target:
            res.append(nums[ind])
            self.rec(ind, nums, target-nums[ind], res)
            res.pop()

        self.rec(ind+1, nums, target, res)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.rec(0, candidates, target, [])
        return self.ans 
        