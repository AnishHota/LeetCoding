# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []

        stack.append([root,-inf,inf])
        while stack:
            vals = stack.pop()
            if vals[0].val<=vals[1] or vals[0].val>=vals[2]:
                return False      
            if vals[0].left:
                stack.append([vals[0].left,vals[1],vals[0].val])
            if vals[0].right:
                stack.append([vals[0].right,vals[0].val,vals[2]])
        
        return True