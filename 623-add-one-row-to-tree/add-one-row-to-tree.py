# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        q = deque()
        q.append(root)
        if depth==1:
            temp = TreeNode(val)
            temp.left = root
            return temp
        depth-=2
        while q:
            if depth==0:
                for _ in range(len(q)):
                    node = q.popleft()
                    
                    temp = node.left
                    node.left = TreeNode(val)
                    node.left.left = temp
                  
                    temp = node.right
                    node.right = TreeNode(val)
                    node.right.right = temp
                return root
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth-=1
        
        return root
