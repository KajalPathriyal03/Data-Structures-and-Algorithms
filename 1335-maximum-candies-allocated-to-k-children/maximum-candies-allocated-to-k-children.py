class Solution:
    def maximumCandies(self, nums: List[int], k: int) -> int:
        l, r=0, 10**7
        while l<r:
            mid=(l+r)//2
            candies=0
            for ele in nums:
                # print((ele//(mid+1)))
                candies+=(ele//(mid+1))
            # print(mid, candies)
            if candies>=k:
                l=mid+1
            else:
                r=mid
        return l
        