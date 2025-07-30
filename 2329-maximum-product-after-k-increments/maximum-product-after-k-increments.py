class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        n=len(nums)
        min_heap=[]
        for ele in nums:
            heappush(min_heap, ele)
        while k:
            mini=heappop(min_heap)
            mini+=1
            heappush(min_heap, mini)
            k-=1
        pro=1
        while min_heap:
            mini=heappop(min_heap)
            pro*=mini%mod
        return pro%mod

        