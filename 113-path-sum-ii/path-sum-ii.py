# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        def dfs(node,rem,path):
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right and node.val==rem:
                self.ans.append(path.copy())
            
            dfs(node.left,rem-node.val,path)
            dfs(node.right,rem-node.val,path)
            path.pop()
            return
        
        dfs(root,targetSum,[])
        return self.ans

