# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        while curr:
            a,b = prev.val, curr.val
            c = gcd(a,b)
            prev.next = ListNode(c)
            prev.next.next = curr
            prev = curr
            curr = curr.next
        
        return head