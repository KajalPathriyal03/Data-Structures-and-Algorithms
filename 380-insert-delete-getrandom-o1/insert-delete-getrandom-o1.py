class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.mp = {} # value: index

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        
        self.mp[val] = len(self.ls)
        self.ls.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        
        index = self.mp[val]
        self.mp[self.ls[-1]] = index
        del self.mp[val]
        self.ls[index] = self.ls[-1]
        self.ls.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.ls) - 1)
        return self.ls[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()