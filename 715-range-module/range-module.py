class RangeModule:

    def __init__(self):
        self.intervals=[]
        

    def addRange(self, left: int, right: int) -> None:
        bisect.insort(self.intervals, [left, right])
        res=[self.intervals[0]]

        for i in range(len(self.intervals)):
            interval=self.intervals[i]

            if res[-1][1]>=interval[0]:
                res[-1][1]=max(res[-1][1], interval[1])
            else:
                res.append(interval)
        self.intervals=res
        

    def queryRange(self, left: int, right: int) -> bool:
        ind=bisect.bisect(self.intervals, [left, int(1e9)])

        if not self.intervals or ind==0:
            return False
            
        return self.intervals[ind-1][1]>=right

    def removeRange(self, left: int, right: int) -> None:
        res=[]
        for interval in self.intervals:
            if left<=interval[0] and right>=interval[1]: continue
            elif left>=interval[1] or right<=interval[0]:
                res.append(interval)
            elif left<=interval[0]:
                res.append([right, interval[1]])
            elif right>=interval[1]:
                res.append([interval[0], left])
            else:
                res.append([interval[0], left])
                res.append([right, interval[1]])
        self.intervals=res

        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)