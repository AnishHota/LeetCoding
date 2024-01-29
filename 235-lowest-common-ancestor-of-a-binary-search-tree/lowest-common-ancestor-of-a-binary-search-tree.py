# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lef = min(p.val,q.val)
        rig = max(p.val,q.val)
        while root:
            if lef<=root.val and rig>=root.val:
                return root
            elif lef>root.val and rig>root.val:
                root = root.right
            else:
                root = root.left
        