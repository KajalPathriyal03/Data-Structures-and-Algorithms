# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
from collections import deque
class PeekingIterator:
    def __init__(self, iterator):
        
        self.queue=deque()
        while iterator.hasNext():
            ele=iterator.next()
            self.queue.append(ele)

        

    def peek(self):
        if self.queue:
            ans = self.queue[0]
            return ans 
        return -1 
        

    def next(self):
        if self.queue:
            return self.queue.popleft()

        return -1 

    def hasNext(self):
        if self.queue:
            return True 
        return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].