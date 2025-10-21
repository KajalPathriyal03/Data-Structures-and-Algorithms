from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.mp={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key]=[]
        self.mp[key].append((timestamp, value))
        # print(self.mp)


    def get(self, key: str, timestamp: int) -> str:
        res=""
        vals=self.mp.get(key, [])
        # print("vals", vals)
        l, r=0, len(vals)-1
        while l<=r:
            mid=(l+r)//2
            if vals[mid][0]<=timestamp:
                res=vals[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)