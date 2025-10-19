"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #1. insert copy nodes in between
        #2 connect random pointers 
        #3 connect next pointers 

        if not head: return None 
        tmp=head 
        while tmp:
            copy=Node(tmp.val)
            copy.next=tmp.next
            tmp.next=copy
            tmp=tmp.next.next
        tmp=head 
        while tmp:
            copy=tmp.next
            if not tmp.random:
                copy.random=None
            else:
                copy.random=tmp.random.next
            tmp=tmp.next.next

        dummy=Node(-1)
        res=dummy
        tmp=head 
        while tmp:
            res.next=tmp.next
            tmp.next=tmp.next.next
            res=res.next
            tmp=tmp.next
        return dummy.next