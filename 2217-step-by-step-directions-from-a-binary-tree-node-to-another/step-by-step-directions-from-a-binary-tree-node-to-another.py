# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ans = ""
        self.start_path = []
        self.end_path = []
        def dfs(node, path):
            if node:
                if node.val == startValue:
                    self.start_path = path[::]
                elif node.val == destValue:
                    self.end_path = path[::]
                if self.start_path and self.end_path:
                    return
                path.append("L")
                dfs(node.left,path)
                path.pop()
                path.append("R")
                dfs(node.right,path)
                path.pop()
        
        dfs(root,[])

        n = min(len(self.start_path),len(self.end_path))
        start_i = 0
        for i in range(n):
            if self.start_path[i] != self.end_path[i]:
                break
            start_i+=1
  
        self.start_path = ''.join(self.start_path[start_i:])
        self.end_path = ''.join(self.end_path[start_i:])
        ans += "U"*len(self.start_path)
        ans += self.end_path

        return ans
