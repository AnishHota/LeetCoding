class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])
        minRow = [float('inf')]*n
        maxCol = [-1]*m
        for i in range(n):
            for j in range(m):
                minRow[i] = min(minRow[i],matrix[i][j])
                maxCol[j] = max(maxCol[j],matrix[i][j])
        
        ans = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==minRow[i] and matrix[i][j]==maxCol[j]:
                    ans.append(matrix[i][j])
        
        return ans
