"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        h = {}

        if not node:
            return node

        def dfs(n):
            if n.val in h:
                return h[n.val]
            
            h[n.val] = Node(n.val)

            for x in n.neighbors:
                h[n.val].neighbors.append(dfs(x))
            
            return h[n.val]
        
        dfs(node)
        return h[node.val]
