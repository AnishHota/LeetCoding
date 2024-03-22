# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        l = 0
        while dummy:
            l+=1
            dummy = dummy.next
        
        arr = []
        dummy = head
        l2 = 0
        while dummy:
            if l%2!=0 and l2==(l-1)//2:
                dummy = dummy.next
                l2+=1
                continue
            elif l2<=(l-1)//2:
                arr.append(dummy.val)
                l2+=1
            elif dummy.val!=arr.pop():
                return False
            dummy = dummy.next 
        return True
        