class Solution:

    def backtracking(self, ind, nums, target, res):
        if ind>=len(nums): return 
        if target<0: return 
        if target==0:
            self.ans.append(res.copy()) 
            return
        res.append(nums[ind])
        self.backtracking(ind, nums, target-nums[ind], res)
        res.pop()
        self.backtracking(ind+1, nums, target, res)     
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.backtracking(0, candidates, target, [])
        return self.ans 