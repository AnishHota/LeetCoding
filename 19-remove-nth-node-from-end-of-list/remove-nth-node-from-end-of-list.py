# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = dummy = head
        p = None
        q = root
        r = root
        while r!=None and n!=0:
            r = r.next
            n-=1
        while r!=None:
            p = q
            q = q.next
            r = r.next
        if not p and q:
            return q.next
        if p and q:
            p.next = q.next
        else:
            return None
        return dummy
        