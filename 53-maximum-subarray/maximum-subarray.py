class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=float('-inf')
        cs=0
        for ele in nums:
            cs+=ele
            if cs>ms:
                ms=cs
            if cs<0:
                cs=0
        return ms        