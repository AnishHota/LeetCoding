# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next
        
        dummy = head
        while stack:
            node = stack.pop()
            node.next = dummy.next
            dummy.next = node
            dummy = dummy.next.next

        dummy.next = None
        