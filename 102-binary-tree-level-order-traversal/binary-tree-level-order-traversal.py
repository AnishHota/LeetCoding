# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        if root:
            queue.append(root)
        else:
            return ans
        
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                x = queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                level.append(x.val)
            ans.append(level)
        return ans
