from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -(self.max_heap[0]):
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if abs(len(self.max_heap)-len(self.min_heap))>1:
            heappush(self.min_heap, -self.max_heap[0])
            heappop(self.max_heap)
        elif len(self.max_heap)<len(self.min_heap):
            heappush(self.max_heap, -self.min_heap[0])
            heappop(self.min_heap)
        
    def findMedian(self) -> float:
        n=len(self.max_heap)
        m=len(self.min_heap)
        # print(self.max_heap, self.min_heap)
        if n==m:
            first, second=(self.max_heap[0]), (self.min_heap[0])
            med=((-first)+second)/2
            return med
        # else
            # ans=heappop(self.max_heap)
        return -self.max_heap[0]
        # return 1.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()