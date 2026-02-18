from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.pq=SortedList()
        for ele in nums:
            self.pq.add(ele)
    def add(self, val: int) -> int:
        self.pq.add(val)            
        return self.pq[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)