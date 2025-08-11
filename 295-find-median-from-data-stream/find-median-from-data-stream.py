class MedianFinder:

    def __init__(self):
        self.nums=[]
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        
    def findMedian(self) -> float:
        n=len(self.nums)
        # print(self.nums)
        self.nums.sort()
        if n%2==0:
            ind=n//2
            med=(self.nums[ind]+self.nums[ind-1])/2
            return med
        else:
            return self.nums[n//2]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()