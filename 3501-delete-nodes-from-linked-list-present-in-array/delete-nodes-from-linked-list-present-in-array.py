# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        pre = ListNode()
        start = pre
        curr = head
        pre.next = curr
        while curr:
            if curr.val in nums:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return start.next
            