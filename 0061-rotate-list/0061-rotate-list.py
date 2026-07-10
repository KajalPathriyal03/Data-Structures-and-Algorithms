# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head 
        n=1
        fast=head

        while fast.next:
            fast=fast.next
            n+=1

        if k==0: return head 
        k=k%n
        cur=head
        
        for _ in range(n-k-1):
            cur=cur.next

        new_head=cur.next 
        cur.next=None
        fast.next=head 
        return new_head


        