class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for ele in nums:
            heappush(pq, ele)
            if len(pq)>k:
                heappop(pq)
        return heappop(pq)
        