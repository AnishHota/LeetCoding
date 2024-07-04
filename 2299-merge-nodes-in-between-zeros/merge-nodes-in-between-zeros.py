# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        s = 0
        while curr!=None:
            if curr.val!=0:
                s += curr.val
            if curr.val==0:
                prev.next = ListNode(s)
                prev = prev.next
                s = 0
            curr = curr.next
        
        return head.next
