# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Maximum height in left subtree + maximum height in right subtree for each node. (Not optimal)
        hei = 1
        max_hei = 0
        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return hei + max(height(root.left),height(root.right))
        
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            curr_hei = height(node.left)+height(node.right)
            if curr_hei>max_hei:
                max_hei = curr_hei
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return max_hei

