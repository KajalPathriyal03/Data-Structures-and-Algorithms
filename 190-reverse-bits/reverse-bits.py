class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            lsb=n&1
            reverseLsb=lsb<<(31-i)
            res|=reverseLsb
            n>>=1
        return res

        