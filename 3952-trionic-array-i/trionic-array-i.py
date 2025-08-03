class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        changes=[]
        for i in range(1, n):
            val=0
            if nums[i]>nums[i-1]:
                val=1
            if nums[i]<nums[i-1]:
                val=-1
            ln=len(changes)
            if val==0:
                return False
            if not changes or changes[-1]!=val:
                changes.append(val)
        if len(changes)==3 and changes[0]==1 and changes[1]==-1 and changes[2]==1:
            return True
        return False
            
