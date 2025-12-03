# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rec(self, l1, l2, cur, temp):
        if l1 is None or l2 is None: 
            if l1: 
                cur.next=l1
            if l2:
                cur.next=l2
            return temp.next
        if l1.val>l2.val: 
            cur.next=l2
            return self.rec(l1, l2.next, cur.next, temp)
        else:
            cur.next=l1
            return self.rec(l1.next, l2, cur.next, temp)


    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-1)  
        cur=temp
        final=self.rec(l1, l2, cur, temp)
        return final

