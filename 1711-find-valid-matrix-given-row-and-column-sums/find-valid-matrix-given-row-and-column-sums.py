class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        a = min(rowSum)
        b = min(colSum)
        n,m = len(rowSum), len(colSum)
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        first_i, first_j = 0,0
        if a<b:
            first_i = rowSum.index(a)
            matrix[first_i][first_j] = a
            rowSum[first_i] -= a
            colSum[first_j] -= a
        else:
            first_j = colSum.index(b)
            matrix[first_i][first_j] = b
            rowSum[first_i] -= b
            colSum[first_j] -= b
        
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    x = min(rowSum[i],colSum[j])
                    matrix[i][j] = x
                    rowSum[i] -=x
                    colSum[j] -=x
        
        return matrix


