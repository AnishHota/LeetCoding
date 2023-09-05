"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        queue = deque()
        queue.append(node)

        visited = {}
        visited[node] = Node(node.val)
        
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()

                for n in temp.neighbors:
                    if n not in visited:
                        visited[n] = Node(n.val)
                        queue.append(n)
                    visited[temp].neighbors.append(visited[n])

        return visited[node]


        