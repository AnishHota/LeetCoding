# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        stack = []
        def postorder(node):
            nonlocal stack
            if not node:
                return None
            postorder(node.left)
            postorder(node.right)
            if node.val not in [2,3]:
                stack.append(node.val)
            else:
                a = stack.pop()
                b = stack.pop()
                if node.val==2:
                    c = a or b
                else:
                    c = a and b
                stack.append(c)
        
        postorder(root)
        return stack[-1]