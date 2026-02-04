# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwo(self, i, j):
        node=ListNode()
        ans=node
        while i and j:
            if i.val > j.val:
                node.next=j
                j=j.next
            else:
                node.next=i
                i=i.next
            node=node.next
        if i:
            node.next=i
        else:
            node.next=j

        return ans.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        ans=[]
        while len(lists)>1:
            merge=[]
            for i in range(0, len(lists), 2):
                l1=lists[i]
                l2=None
                if i+1<len(lists):
                    l2=lists[i+1]
                merge.append(self.mergeTwo(l1, l2))
            
            lists=merge
        return lists[0]