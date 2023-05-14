# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        p = None
        q = head
        r = q.next
        if r is None:
            return q
        
        while r!=None:
            q.next = p
            p=q
            q=r
            r = r.next
        
        q.next = p
        return q