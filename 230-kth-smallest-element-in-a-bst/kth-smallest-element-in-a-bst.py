# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ino = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.ino.append(node.val)
                inorder(node.right)
        
        inorder(root)
        heap = heapq.nsmallest(k,self.ino)
        heap = heapq.nlargest(1,heap)
        return heapq.heappop(heap)