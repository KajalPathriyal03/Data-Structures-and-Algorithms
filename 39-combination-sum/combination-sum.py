class Solution:
    def solve(self, i, nums, target, cur_sum, res):
        if cur_sum==target:
            self.ans.append(res.copy())
            return 
        if i>=len(nums) or cur_sum>target:
            return 
        res.append(nums[i])
        self.solve(i, nums, target, cur_sum+nums[i], res)
        res.pop()
        self.solve(i+1, nums, target, cur_sum, res)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        res=[]
        self.solve(0,candidates, target, 0, res)
        return self.ans
        