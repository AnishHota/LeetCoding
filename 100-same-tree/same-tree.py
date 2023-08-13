# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = []
        q2 = []

        q1.append(p)
        q2.append(q)

        while q1 and q2:
            node1 = q1.pop()
            node2 = q2.pop()

            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                
                q1.append(node1.left)
                q2.append(node2.left)
                q1.append(node1.right)
                q2.append(node2.right)
        
        if q1 or q2:
            return False
        
        return True
        