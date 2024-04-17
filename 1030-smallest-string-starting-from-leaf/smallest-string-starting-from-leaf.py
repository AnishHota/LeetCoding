# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node,s,small):
            if not node:
                return 
            s.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                curr = ''.join(s[::-1])
                if small[0]>curr:
                    small[0]=curr
            
            dfs(node.left,s,small)
            dfs(node.right,s,small)

            s.pop()
        
        small = [chr(ord('z')+1)]
        dfs(root,[],small)
        return small[0]
        