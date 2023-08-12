# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.isBal = True
        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            if abs(left-right)>1:
                self.isBal = False
            return max(left,right)+1

        depth(root)
        return self.isBal      