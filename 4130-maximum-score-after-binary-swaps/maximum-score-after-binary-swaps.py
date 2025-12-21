class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        sm=0
        pq=[]
        for i, ele in enumerate(s):
            heappush(pq,  -nums[i])
            if ele=="1":
                sm+=(-heappop(pq))

        return sm
        