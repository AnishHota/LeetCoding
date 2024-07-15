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
            if p not in tree:
                tree[p] = TreeNode(p)
            if il==1:
                if c in tree:
                    tree[p].left = tree[c]
                else:
                    tree[c] = TreeNode(c)
                    tree[p].left = tree[c]
            else:
                if c in tree:
                    tree[p].right = tree[c]
                else:
                    tree[c] = TreeNode(c)
                    tree[p].right = tree[c]

        for p,_,_ in descriptions:
            if p not in child:
                return tree[p]   
            

