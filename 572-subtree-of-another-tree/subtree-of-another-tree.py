# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return p.val==q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        self.ans = False
        def inorder(node):
            if node:
                inorder(node.left)
                ans = isSameTree(node,subRoot)
                if ans == True:
                    self.ans = True
                    return
                inorder(node.right)
        
        inorder(root)
        return self.ans
