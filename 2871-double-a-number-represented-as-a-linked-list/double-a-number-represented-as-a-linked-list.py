# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = head
        if head and head.val>4:
            node = ListNode(1,head)
            ans = node
        
        while head:
            head.val = (head.val*2)%10 
            if head.next and head.next.val>4:
                head.val+=1
            head = head.next

        return ans     

        