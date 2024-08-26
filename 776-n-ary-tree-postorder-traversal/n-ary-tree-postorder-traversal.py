"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def post(node):
            if node:
                for x in node.children:
                    post(x)
                ans.append(node.val)
        
        post(root)
        return ans