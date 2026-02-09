# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pt1, pt2=headA, headB
        mp={}

        while pt1:
            mp[pt1]=pt1.val
            pt1=pt1.next

        while pt2:
            if pt2 in mp:
                return pt2
            pt2=pt2.next

        return None
        