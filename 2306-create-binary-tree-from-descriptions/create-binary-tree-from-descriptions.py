# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = defaultdict()
        child = set()
        for p,c,il in descriptions:
            child.add(c)
            parentNode = tree.setdefault(p,TreeNode(p))
            childNode = tree.setdefault(c,TreeNode(c))
            if il==1: 
                parentNode.left = childNode
            else:
                parentNode.right = childNode

        for p,_,_ in descriptions:
            if p not in child:
                return tree[p]   
            

