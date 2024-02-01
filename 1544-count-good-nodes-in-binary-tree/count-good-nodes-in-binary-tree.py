# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNode = 0
        maxVal = -inf
        stack = [(root,maxVal)]

        while stack:
            node, maxVal = stack.pop()
            if node.val>=maxVal:
                goodNode+=1
            if node.left:
                stack.append((node.left,max(maxVal,node.val))) 
            if node.right:
                stack.append((node.right,max(maxVal,node.val)))
        
        return goodNode
