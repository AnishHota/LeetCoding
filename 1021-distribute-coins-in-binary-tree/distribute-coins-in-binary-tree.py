# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            l_extra = dfs(node.left)
            r_extra = dfs(node.right)
            extra = node.val + l_extra + r_extra - 1
            self.res += abs(extra)
            return extra
        
        dfs(root)
        return self.res
