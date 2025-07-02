class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        odd, even, alternate=0, 0, 0
        flag=-1
        for i in range(n):
            if nums[i]%2==0:
                even+=1
                if flag!=1:
                    alternate+=1
                    flag=1
            else:
                odd+=1
                if flag!=0:
                    alternate+=1
                    flag=0
        return max(even, odd, alternate)
        
        
        