# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.inOrder = []

        def iotrav(node):
            if node:
                iotrav(node.left)
                self.inOrder.append(node.val)
                iotrav(node.right)
        
        iotrav(root)
        postSum = [0]*len(self.inOrder)
        postSum[-1]=self.inOrder[-1]
        for i in range(len(self.inOrder)-2,-1,-1):
            postSum[i] = postSum[i+1]+self.inOrder[i]
        
        self.i = 0
        def change(node):
            if node:
                change(node.left)
                node.val = postSum[self.i]
                self.i+=1
                change(node.right)
        
        change(root)
        return root
