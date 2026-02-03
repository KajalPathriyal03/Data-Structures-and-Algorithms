class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
    def addNum(self, num: int) -> None:
        if not self.maxHeap or num<(-self.maxHeap[0]):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
            
        if abs(len(self.maxHeap)-len(self.minHeap))>1:
            top=self.maxHeap[0]
            heappush(self.minHeap, -top)
            heappop(self.maxHeap)
        
        elif len(self.maxHeap)<len(self.minHeap):
            top=self.minHeap[0]
            heappush(self.maxHeap, -top)
            heappop(self.minHeap)

    def findMedian(self) -> float:
        if len(self.maxHeap)==len(self.minHeap):
            return (-(self.maxHeap[0])+self.minHeap[0])/2
        return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()