# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        s = defaultdict(int)
        s[0] = 0
        s[1] = 0
        q.append(root)
        level = 1
        while q:
            curr = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    curr += node.left.val
                    q.append(node.left)
                if node.right:
                    curr += node.right.val
                    q.append(node.right)
            s[level]+=curr
            level+=1
    

        q = deque()
        q.append(root)
        level = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                a,b = 0,0
                if node.left:
                    a = node.left.val
                    q.append(node.left)
                if node.right:
                    b = node.right.val
                    q.append(node.right)
                chnge = s[level]-a-b
                if node.left:
                    node.left.val = chnge
                if node.right:
                    node.right.val = chnge
            level+=1
        root.val = 0
        return root