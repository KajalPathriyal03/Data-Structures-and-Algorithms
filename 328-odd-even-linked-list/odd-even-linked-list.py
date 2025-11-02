# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode(-1)
        oddTail=odd
        even=ListNode(-1)
        evenTail=even
        cur=head
        temp=head
        t=0
        while cur:
            temp=cur 
            cur=cur.next
            temp.next=None 
            
            if t & 1:
                oddTail.next=temp
                oddTail=temp
            else:
                evenTail.next=temp
                evenTail=temp
            t+=1
        evenTail.next=odd.next
        return even.next


        