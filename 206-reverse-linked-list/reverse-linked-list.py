# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p,q,r = None, head, head.next

        while q:
            q.next = p
            p = q
            q = r
            r = r.next if r else None
        
        return p