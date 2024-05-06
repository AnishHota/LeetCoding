# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            if not stack:
                stack.append((node, node.val))
            else:
                while stack and node.val > stack[-1][1]:
                    stack.pop()
                stack.append((node,node.val))
            node = node.next
        
        temp = ListNode()
        new_head = temp
        for x in stack:
            temp.next = x[0]
            temp = temp.next
        
        temp.next = None
        return new_head.next

        