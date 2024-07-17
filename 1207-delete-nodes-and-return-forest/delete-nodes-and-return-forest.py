# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        
        self.forest = []
        if root.val not in to_delete:
            self.forest.append(root)
    
        def postorder(node):
            if node:
                left = postorder(node.left)
                right = postorder(node.right)
                if not left:
                    node.left = None
                if not right:
                    node.right = None
                if node.val in to_delete:
                    if node.left:
                        self.forest.append(node.left)
                    if node.right:
                        self.forest.append(node.right)
                    return None
                return node

        
        postorder(root)

        return self.forest