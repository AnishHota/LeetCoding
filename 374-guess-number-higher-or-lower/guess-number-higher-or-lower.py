# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i,j = 1,n
        while i<=j:
            g = int(i+(j-i)/2)
            r = guess(g)
            if r==-1:
                j = g-1
            elif r==1:
                i = g+1
            else:
                return g
