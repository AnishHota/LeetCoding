# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode()
        curr = rem = 0
        while l1 or l2:
            curr = 0
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            curr += rem
            root.next = ListNode(curr%10)
            rem = curr//10
            root = root.next
            
        if rem:
            root.next = ListNode(rem)
        
        return head.next