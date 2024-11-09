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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head==None:
            return None
        
        if head.next == None:
            return TreeNode(head.val)
        
        # Get Middle
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        
        root.right = self.sortedListToBST(slow.next)
        slow.next = None
        root.left = self.sortedListToBST(head)

        return root        