class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        streak=0
        cnt=0
        for ele in nums:
            if ele==0:
                streak+=1
            else:
                streak=0
            cnt+=streak
        return cnt

        