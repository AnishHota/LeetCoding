# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = end = head

        for _ in range(n):
            end = end.next

        if not end: return head.next

        while end.next:
            end = end.next
            node = node.next

        node.next = node.next.next
        return head   