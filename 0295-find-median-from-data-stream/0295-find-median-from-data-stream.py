class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if not self.maxheap or -self.maxheap[0]>num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        if len(self.maxheap)-len(self.minheap)>1:
            top=heappop(self.maxheap)
            heappush(self.minheap, -top)
        
        elif len(self.minheap)>len(self.maxheap):
            top=heappop(self.minheap)
            heappush(self.maxheap, -top)
        

    def findMedian(self) -> float:
        if len(self.minheap)!=len(self.maxheap):
            return -self.maxheap[0]

        sm=(self.minheap[0]+(-self.maxheap[0]))/2
        return sm
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
