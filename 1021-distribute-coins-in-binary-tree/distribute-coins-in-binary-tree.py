# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node, size, coins):
            nonlocal res
            if not node:
                return 0,0
            
            if not node.left and not node.right:
                return (1,node.val)
            
            x,y = dfs(node.left,size,coins)
            a,b = dfs(node.right,size,coins)
            res += abs(y-x) + abs(b-a)
            size += x+a
            coins += b+y+node.val-1
            return (size,coins)
        
        dfs(root,0,0)
        return res
