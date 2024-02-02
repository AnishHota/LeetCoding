# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        
        def build(preorder,inorder):
            if len(inorder)==0:
                return None
            node = preorder.pop()
            index = inorder.index(node)
            root = TreeNode(node)
            root.left = build(preorder,inorder[:index])
            root.right = build(preorder,inorder[index+1:])
            return root

        return build(preorder,inorder)

        