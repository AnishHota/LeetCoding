# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast!=None:
            i=0
            slow=slow.next
            while fast!=None and i!=2:
                fast = fast.next
                i+=1
            
        return slow