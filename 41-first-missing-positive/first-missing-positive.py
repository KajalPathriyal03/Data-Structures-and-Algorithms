from sortedcontainers import  SortedSet
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        contains_one=False 
        for i in range(len(nums)):
            if nums[i]==1:
                contains_one=True
            if nums[i]<=0:
                nums[i]=1
            if nums[i]>n:
                nums[i]=1
        if not contains_one:
            return 1
        
        for i in range(n):
            num=abs(nums[i])
            ind=num-1
            if nums[ind]<0:
                continue
            nums[ind]*=-1
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
