"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        arr = {}
        dummy = head
        ans = Node(-1)
        prev = ans
        while dummy:
            curr = Node(dummy.val)
            arr[dummy] = curr
            if dummy.random in arr:
                curr.random = arr[dummy.random]
            prev.next = curr
            prev=curr
            dummy = dummy.next
        
        dummy = head
        temp = ans.next
        while dummy:
            if not temp.random and dummy.random in arr:
                temp.random = arr[dummy.random]
            temp = temp.next
            dummy = dummy.next
        return ans.next
        

        