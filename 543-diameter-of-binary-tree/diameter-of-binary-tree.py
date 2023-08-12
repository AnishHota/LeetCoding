# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        @cache
        def depth(node):
            if not node:
                return 0
            
            return max(depth(node.left),depth(node.right))+1
        
        queue = collections.deque()
        queue.append(root)
        maxDiam = 0
        while queue:
            node = queue.popleft()
            diam = depth(node.left)+depth(node.right)

            if diam>maxDiam:
                maxDiam = diam
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return maxDiam
            
        