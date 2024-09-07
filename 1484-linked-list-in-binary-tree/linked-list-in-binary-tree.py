# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(node,temp):
            if not temp:
                return True
            if not node:
                return False
            if node.val!=temp.val:
                return False
            
            return dfs(node.left,temp.next) or dfs(node.right,temp.next)


        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == head.val:
                temp = head
                if dfs(node,temp):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False