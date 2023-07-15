# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Maximum height in left subtree + maximum height in right subtree for each node. (Not optimal)
        self.diam = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            if (left+right)>self.diam:
                self.diam = left+right
            
            return 1+max(left,right)

        height(root)
        return self.diam
        
        # queue = collections.deque()
        # queue.append(root)

        # while queue:
        #     node = queue.popleft()
        #     curr_hei = height(node.left)+height(node.right)
        #     if curr_hei>max_hei:
        #         max_hei = curr_hei
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        return diam

