class Solution:
    def rec(self, ind, nums, res):
        self.ans.append(res.copy())
        
        for i in range(ind, len(nums)):
            if i>ind and nums[i-1]==nums[i]:
                continue 
            res.append(nums[i])
            self.rec(i+1, nums, res)
            res.pop()

    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        nums.sort()
        self.rec(0, nums, [])
        return list(self.ans )
        