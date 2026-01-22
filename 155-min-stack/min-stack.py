class MinStack:

    def __init__(self):
        self.mini=float('inf')
        self.nums=[]

    def push(self, val: int) -> None:
        self.nums.append(val)
        self.mini=min(self.mini, val)

    def pop(self) -> None:
        self.nums.pop(-1)
        if self.nums:
            self.mini=min(self.nums)
        else:
            self.mini=float('inf')
        
    def top(self) -> int:
        return self.nums[-1]
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()