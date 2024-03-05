class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        a,b = 0,r-1

        while a<=b:
            mid = int(b+(a-b)/2)
            if target == matrix[mid][0]:
                return True
            elif target<matrix[mid][0]:
                b=mid-1
            elif target>matrix[mid][-1]:
                a=mid+1
            else:
                p,q = 0,c-1
                while p<=q:
                    midR = int(q + (p-q)/2)
                    if target==matrix[mid][midR]:
                        return True
                    elif target>matrix[mid][midR]:
                        p=midR+1
                    else:
                        q=midR-1
                return False
        return False

        