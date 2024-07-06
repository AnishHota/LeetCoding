# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = min(p.val,q.val)
        right = max(p.val,q.val)
        while root:
            if root.val>=left and root.val<=right:
                return root
            elif root.val>left and root.val>right:
                root = root.left
            else:
                root = root.right