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
        if not head:
            return head
        
        hash = {}
        dummy = head
        while dummy:
            curr = Node(dummy.val)
            hash[dummy] = curr
            dummy = dummy.next
        
        dummy = head
        while dummy:
            hash[dummy].next = hash.get(dummy.next)
            hash[dummy].random = hash.get(dummy.random)
            dummy = dummy.next
        return hash[head]
        

        