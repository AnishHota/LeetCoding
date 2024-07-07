class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        t = int(numBottles/numExchange)
        while t>=1:
            ans += t
            rem = numBottles%numExchange
            numBottles = t+rem
            t = int(numBottles/numExchange)
        return ans