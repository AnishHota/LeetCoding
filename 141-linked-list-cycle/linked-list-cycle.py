# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            p = head
            q = head.next
        else:
            return False

        while q!=None:
            if p==q:
                return True
            p = p.next
            if q.next:
                q = q.next.next
            else:
                return False
        return False