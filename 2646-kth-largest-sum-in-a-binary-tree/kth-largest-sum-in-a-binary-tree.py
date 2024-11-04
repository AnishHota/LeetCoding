# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = deque()
        q.append(root)
        while q:
            curr = 0
            for i in range(len(q)):
                node = q.popleft()
                curr += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heappush(heap,-curr)
        
        if len(heap)<k:
            return -1

        while k!=1:
            heappop(heap)
            k-=1
        return -heappop(heap)        