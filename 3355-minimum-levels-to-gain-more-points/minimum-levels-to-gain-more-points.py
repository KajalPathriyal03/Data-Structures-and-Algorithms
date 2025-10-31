class Solution:
    def minimumLevels(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1
        sm=sum(nums)
        pre=0
        ans=-1
        for i in range(n-1):
            pre+=nums[i]
            if pre>sm-pre:
                return i+1
        return ans

                
                
                
            
        