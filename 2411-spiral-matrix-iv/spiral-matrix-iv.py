# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        a,b = 0,1
        arr = [[-1 for _ in range(n)] for _ in range(m)]
        i,j = 0,0
        while head:
            for j in range(a,n-a):
                arr[i][j] = head.val
                head = head.next
                if not head:
                    return arr
            
            for i in range(b,m-a):
                arr[i][j]=head.val
                head = head.next
                if not head:
                    return arr
            
            for j in range(n-b-1,a-1,-1):
                arr[i][j]=head.val
                head = head.next
                if not head:
                    return arr
            
            for i in range(m-b-1,b-1,-1):
                arr[i][j]=head.val
                head = head.next
                if not head:
                    return arr
            a+=1
            b+=1

        return arr