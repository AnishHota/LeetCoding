# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import os
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.leafNodes = []

        def inorder(node, path):
            if node:
                inorder(node.left, path+['L'])
                if not node.left and not node.right:
                    self.leafNodes.append(''.join(path))
                inorder(node.right,path+['R'])

        inorder(root,[])

        self.ans = 0

        n = len(self.leafNodes)
        for i in range(n):
            for j in range(i+1,n):
                k = len(os.path.commonprefix([self.leafNodes[i],self.leafNodes[j]]))
                temp_d = len(self.leafNodes[i])-k+len(self.leafNodes[j])-k
                if temp_d<=distance:
                    self.ans+=1

        return self.ans
        

