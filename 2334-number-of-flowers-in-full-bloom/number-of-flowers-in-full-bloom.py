class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n=len(people)
        people=[(ele, i) for i, ele in enumerate(people)]
        res=[0 for _ in range(n)]
        start=[f[0] for f in flowers]
        end=[f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)
        cnt=0
        for ele, i in sorted(people):
            while start and start[0]<=ele:
                heappop(start)
                cnt+=1
            while end and end[0]<ele:
                heappop(end)
                cnt-=1
            res[i]=cnt
        return res

        