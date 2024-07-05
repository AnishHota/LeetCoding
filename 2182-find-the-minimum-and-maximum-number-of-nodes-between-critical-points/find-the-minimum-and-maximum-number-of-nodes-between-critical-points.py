# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p = head
        q = head.next
        r = q.next
        ans = [-1,-1]
        if p is None or q is None or r is None:
            return ans
        
        cpoints = []
        i = 1
        ans[0] = float('inf')
        while r:
            if q.val<p.val and q.val<r.val:
                cpoints.append(i)
            elif q.val>p.val and q.val>r.val:
                cpoints.append(i)
            if len(cpoints)>=2:
                    ans[0] = min(ans[0],cpoints[-1]-cpoints[-2])
            i+=1
            p = p.next
            q = q.next
            r = r.next
        
        if len(cpoints)>=2:
            ans[1] = cpoints[-1]-cpoints[0]
            return ans
        
        return [-1,-1]