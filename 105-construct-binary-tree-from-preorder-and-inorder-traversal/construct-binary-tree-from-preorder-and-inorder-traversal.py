# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderid = 0
        dic = {e:i for i,e in enumerate(inorder)}

        def build(preorder,inorder,beg,end):
            nonlocal preorderid
            if beg>end:
                return None
            node = preorder[preorderid]
            preorderid+=1
            index = dic[node]
            root = TreeNode(node)
            root.left = build(preorder,inorder,beg,index-1)
            root.right = build(preorder,inorder,index+1,end)
            return root

        return build(preorder,inorder,0,len(inorder)-1)

        