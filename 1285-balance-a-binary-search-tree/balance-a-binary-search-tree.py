# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inOr = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                self.inOr.append(root.val)
                inOrder(root.right)
        
        inOrder(root)
        self.inOr.sort()

        def balance(i,j):
            if i<=j:
                mid = int(i + (j-i)/2)
                node = TreeNode(self.inOr[mid])
                node.left = balance(i,mid-1)
                node.right = balance(mid+1,j)
                return node
            else:
                return None

        return balance(0,len(self.inOr)-1)


