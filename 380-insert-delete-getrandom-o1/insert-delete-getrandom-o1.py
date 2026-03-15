class RandomizedSet:

    def __init__(self):
        self.ls=[]
        self.mp={}

    def insert(self, val: int) -> bool:
        if val in self.mp: return False 

        self.mp[val]=len(self.ls)
        self.ls.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False 

        del_ind=self.mp[val]
        last_element=self.ls[-1]
        self.mp[last_element]=del_ind
        del self.mp[val]

        self.ls[del_ind]=last_element
        self.ls.pop()
        return True 

    def getRandom(self) -> int:
        ind=random.randint(0, len(self.ls)-1)
        return self.ls[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()