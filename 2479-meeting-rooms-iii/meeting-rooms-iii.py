class Solution:
    def mostBooked(self, n: int, nums: List[List[int]]) -> int:
        mp= [0] * n
        pq=list(range(n))
        heapify(pq)
        min_heap=[]
        for start, end in sorted(nums):
            while min_heap and min_heap[0][0]<=start:
                time, room=heappop(min_heap)
                heappush(pq, room)
            if pq:
                room=heappop(pq)
                heappush(min_heap, [end, room])
            else:
                time, room =heappop(min_heap)
                heappush(min_heap, [time+end-start, room])
            mp[room]+=1
        return mp.index(max(mp))






