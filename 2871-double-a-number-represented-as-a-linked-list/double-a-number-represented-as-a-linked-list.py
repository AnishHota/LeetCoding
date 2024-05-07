# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(100000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        number = 0
        temp = head
        while temp:
            number = number*10+temp.val
            temp = temp.next
        
        number *= 2
        number = list(str(number))
        i=0
        temp = head
        while temp:
            temp.val = int(number[i])
            i+=1
            if temp.next:
                temp = temp.next
            else:
                break
            
        
        while i<len(number):
            node = ListNode(int(number[i]))
            temp.next = node
            temp = temp.next
            i+=1
        
        temp.next = None
        return head
