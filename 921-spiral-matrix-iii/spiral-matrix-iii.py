class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        ans = [[rStart,cStart]]
        add = True
        for i in range(1,(rows+1) * (cols+1)):    
            for j in range(i):
                cStart = cStart + 1 if add else cStart - 1
                if (rStart>=0 and rStart<rows) and (cStart>=0 and cStart<cols):
                    ans.append([rStart,cStart])

            for j in range(i):
                rStart = rStart + 1 if add else rStart - 1
                if (rStart>=0 and rStart<rows) and (cStart>=0 and cStart<cols):
                    ans.append([rStart,cStart])
            if len(ans) == rows*cols:
                break
            add = not add

        return ans
            