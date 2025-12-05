class Solution:
    def rec(self, nums):
        prev=0
        prev2=0
        for ele in nums:
            take=ele+prev2
            not_take=prev
            cur=max(take, not_take)
            prev2=prev
            prev=cur 
        return prev
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        arr=nums
        front=self.rec(arr[:len(nums)-1])
        back=self.rec(arr[1:])
        return max(front, back)
        