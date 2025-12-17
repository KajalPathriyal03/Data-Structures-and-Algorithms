class Solution:
    def rec(self, ind, nums, target):
        if target==0:
            return 1
        if ind>=len(nums): return 0
        if (ind, target) in self.dp:
            return self.dp[(ind, target)]
        not_take=self.rec(ind+1, nums, target)
        take=0
        if nums[ind]<=target:
            take=self.rec(ind, nums, target-nums[ind])
        self.dp[(ind, target)]= take+not_take 
        return self.dp[(ind, target)]
    def change(self, amount: int, coins: List[int]) -> int:
        self.dp={}
        return self.rec(0, coins, amount)