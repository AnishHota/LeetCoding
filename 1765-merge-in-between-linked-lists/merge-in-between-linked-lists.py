# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = 0
        q = 0
        temp1 = list1
        while q!=b+1:
            p+=1
            q+=1
            if p==a:
                startNode = temp1
            temp1=temp1.next
        
        temp2 = list2
        while temp2.next:
            temp2=temp2.next
        startNode.next = list2
        temp2.next = temp1
        return list1