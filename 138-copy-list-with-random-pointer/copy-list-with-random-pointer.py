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
        if not head:
            return None
        
        ans={}
        dummy=head
        while dummy:
            ans[dummy]=Node(dummy.val)
            dummy=dummy.next
        # print(ans)
        dummy=head
        while dummy:
            ans[dummy].next=ans.get(dummy.next)
            ans[dummy].random=ans.get(dummy.random)
            dummy=dummy.next
        return ans[head]