class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        a = min(rowSum)
        b = min(colSum)
        n,m = len(rowSum), len(colSum)
        matrix = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                x = min(rowSum[i],colSum[j])
                matrix[i][j] = x
                rowSum[i] -=x
                colSum[j] -=x
        
        return matrix


