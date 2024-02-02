# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(node,k):
            if node:
                inorder(node.left,k)
                arr.append(node.val)
                k-=1
                if k==0:
                    return arr[-1]
                inorder(node.right,k)

        inorder(root,k)
        return arr[k-1]
        