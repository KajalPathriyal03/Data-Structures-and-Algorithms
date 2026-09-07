class Solution:
    def rec(self, ind, nums, w, res):
        if w==0:
            self.ans.append(res.copy())
            return 

        for i in range(ind, len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue 
            if nums[i]>w:
                break 

            res.append(nums[i])
            self.rec(i+1, nums, w-nums[i], res)
            res.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        candidates.sort()
        self.rec(0, candidates, target, [])
        return self.ans 
        