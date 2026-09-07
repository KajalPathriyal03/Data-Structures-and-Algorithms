class Solution:
    def rec(self, ind, nums, w, res):
        if w==0:
            self.ans.append(res.copy())
            return 
        if ind>=len(nums) or w<0:
            return 

        res.append(nums[ind])
        self.rec(ind, nums, w-nums[ind], res)
        res.pop()
        self.rec(ind+1, nums, w, res)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.target=target
        self.rec(0, candidates, target, [])
        return self.ans
        