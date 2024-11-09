# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        if not head:
            return None
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l+=1
        k = k%l

        while k:
            fast = fast.next
            k -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = head
        temp = slow.next
        slow.next = None
        return temp