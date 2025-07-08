class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n=len(nums)
        m = defaultdict(int)
        digits=0
        for x in nums:
            if x == 0:
                m[(0, 0)] += 1
                continue

            ind = 0
            while x > 0:
                digit = x % 10
                m[(digit, ind)] += 1
                ind += 1
                x //= 10
            
            digits=ind
        ans=((n*(n-1))//2)*digits

        for ele, cnt in m.items():
            ans-=(cnt*(cnt-1))//2
        return ans