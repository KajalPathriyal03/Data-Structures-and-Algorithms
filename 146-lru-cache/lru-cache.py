class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None 
class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(-1, -1)
        self.tail=Node(-1, -1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mp={}
        self.n=capacity
        
    def insert(self, node):
        tmp=self.head.next
        
        node.next=tmp
        node.prev=self.head
        self.head.next=node
        tmp.prev=node
        
    def delete(self, delNode):
        prevv=delNode.prev
        nextt=delNode.next
        prevv.next=nextt
        nextt.prev=prevv
         
    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1 
        ans=-1
        node=self.mp[key]
        ans=node.val
        del self.mp[key]
        self.delete(node)
        self.insert(node)
        self.mp[key]=self.head.next
        
        return ans 
            
            
    def put(self, key: int, val: int) -> None:
        if key in self.mp:
            curNode=self.mp[key]
            del self.mp[key]
            self.delete(curNode)
        
        if len(self.mp)==self.n:
            node=self.tail.prev
            del self.mp[node.key]
            self.delete(node)
        
        curNode=Node(key, val)
        self.insert(curNode)
        self.mp[key]=self.head.next
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)