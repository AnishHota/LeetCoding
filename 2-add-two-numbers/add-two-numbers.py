# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        num1=''
        while head1:
            num1+=str(head1.val)
            head1 = head1.next
        head2 = l2
        num2=''
        while head2:
            num2+=str(head2.val)
            head2 = head2.next
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        ans = num1+num2
        ans = list(str(ans)[::-1])
        ansHead = dummy = None
        for x in ans:
            temp = ListNode(int(x))
            if dummy:
                dummy.next = temp
                dummy = dummy.next
            else:
                dummy = temp
                ansHead = dummy
        dummy.next = None        
        return ansHead