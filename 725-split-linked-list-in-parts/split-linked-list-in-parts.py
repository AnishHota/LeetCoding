# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        lin_len = 0
        while temp:
            lin_len +=1
            temp = temp.next
        
        if lin_len==0:
            return [ListNode(val='')]*k

        ans = []
        if lin_len<k:
            temp = head
            n = temp.next
            while temp:
                temp.next = None
                ans.append(temp)
                temp = n
                if n:
                    n = n.next
            for _ in range(k-lin_len):
                ans.append(ListNode(val=''))
            return ans
        
        rem = lin_len % k
        each = lin_len//k
        temp = head
        n = temp.next
        while temp:
            ans.append(temp)
            for _ in range(each-1):
                temp = temp.next
                if n:
                    n = n.next
            if rem!=0:
                temp = temp.next
                n = n.next
                rem -= 1
            temp.next = None
            temp = n
            if n:
                n = n.next

        return ans

        
