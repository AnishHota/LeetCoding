class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r,c = len(points), len(points[0])

        def left(arr):
            lft = [0]*len(arr)
            lft[0]=arr[0]
            for i in range(1,len(arr)):
                lft[i]=max(lft[i-1]-1,arr[i])
            return lft
        
        def right(arr):
            rgt = [0]*len(arr)
            rgt[-1]=arr[-1]
            for i in range(len(arr)-2,-1,-1):
                rgt[i] = max(rgt[i+1]-1,arr[i])
            return rgt

        pre = points[0]
        curr = [0]*c
        for i in range(r-1):
            lft, rgt = left(pre), right(pre)
            curr = [0]*c
            for j in range(c):
                curr[j] = points[i+1][j] + max(lft[j],rgt[j])
            pre = curr[:]
        
        return max(pre)
        
