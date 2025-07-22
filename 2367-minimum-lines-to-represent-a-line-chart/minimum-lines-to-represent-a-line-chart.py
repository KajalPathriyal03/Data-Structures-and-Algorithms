from decimal import Decimal
class Solution:
    def minimumLines(self, nums: List[List[int]]) -> int:
        n=len(nums)
        if n==1: return 0
        nums.sort()
        cnt=1
        slope=Decimal(nums[1][1]-nums[0][1])/Decimal(nums[1][0]-nums[0][0])
        for i in range(2, n ):
            neu, deno=(nums[i][1]-nums[i-1][1]), (nums[i][0]-nums[i-1][0])
            new=Decimal(neu)/Decimal(deno)
            print(i, new, slope, cnt)
            if new!=slope:
                slope=new
                cnt+=1
            
        return cnt
