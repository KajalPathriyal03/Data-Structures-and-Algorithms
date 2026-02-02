class Solution:
    def backtrack(self, nums, ans):
        if len(ans)==len(nums):
            self.res.append(ans.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in ans:
                    continue 
                ans.append(nums[i])
                self.backtrack(nums, ans)
                ans.pop()

            
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        ans=[]
        self.backtrack(nums, ans)
        return self.res

        