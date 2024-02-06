class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)-1
        c = len(matrix[0])-1
        rowP = 0
        colP = 0
        while rowP<=r:
            mid = (r+rowP)//2
            if target>matrix[mid][-1]:
                rowP = mid+1
            elif target<matrix[mid][0]:
                r = mid-1
            else:
                break

        if rowP>r:
            return False
        row = (r+rowP)//2


        while colP<=c:
            mid = (c+colP)//2
            if target==matrix[row][mid]:
                return True
            if target>matrix[row][mid]:
                colP+=1
            else:
                c-=1

        return False

