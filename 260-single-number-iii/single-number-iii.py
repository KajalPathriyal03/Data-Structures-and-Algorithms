class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorr=0

        for ele in nums:
            xorr^=ele 

        diffBit=xorr & -xorr

        a, b=0, 0
        for ele in nums:
            if ele&diffBit:
                a^=ele
            else:
                b^=ele

        return [a,b]
        