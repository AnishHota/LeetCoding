class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div = int(time/(n-1))
        rem = time%(n-1)
        if div%2==0:
            return 1+rem
        else:
            return n-rem