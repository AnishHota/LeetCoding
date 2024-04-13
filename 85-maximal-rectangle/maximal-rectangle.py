class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=int(matrix[i][j])
        
        stack = []
        rect_row, ans = 0,0
        start = 0
        for i in range(rows):
            stack.clear()
            rect_row = 0
            for j in range(cols):
                start = j
                if i==0:
                    while stack and stack[-1][1]>matrix[i][j]:
                        ind, height = stack.pop()
                        rect_row = max((j-ind)*height,rect_row)
                        start = ind
                    stack.append((start,matrix[i][j]))
                else:
                    if matrix[i][j]==1:
                        matrix[i][j] += matrix[i-1][j]
                    while stack and stack[-1][1]>matrix[i][j]:
                        ind,height = stack.pop()
                        rect_row = max((j-ind)*height,rect_row)
                        start = ind
                    stack.append((start,matrix[i][j]))
            ans = max(rect_row,ans)
            for ind,height in stack:
                ans = max((cols-ind)*height,ans)
        return ans