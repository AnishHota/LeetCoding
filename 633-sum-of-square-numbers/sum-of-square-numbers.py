class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = floor(c**(1/2))

        i,j = 0,n
        while i<=j:
            if i*i + j*j > c:
               j-=1
            elif i*i + j*j <c:
                i+=1
            else:
                return True

        return False 
        