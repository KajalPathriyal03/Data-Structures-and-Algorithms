class NumArray:

    def __init__(self, nums: List[int]):
        self.pref=[ele for ele in nums]
        for i in range(1, len(nums)):
            self.pref[i]=self.pref[i-1]+nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        ans =0
        if left>0:
            ans = self.pref[right]-self.pref[left-1]
        else:
            ans = self.pref[right]
        return ans 
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)