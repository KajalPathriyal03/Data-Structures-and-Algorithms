class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False 

class Trie:

    def __init__(self):
        self.root=Node()
        
    def insert(self, word: str) -> None:
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                cur.links[idx]=Node()
            cur=cur.links[idx]

        cur.flag=True 
    
    def search(self, word: str) -> bool:
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                return False 
            cur=cur.links[idx]
        return cur.flag==True  

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for ch in prefix:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                return False 
            cur=cur.links[idx]
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)