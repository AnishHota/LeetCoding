class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        result = x
        rem = n-1
        position = 1

        while rem:
            if not (x&position):
                result |= (rem&1)*position
                rem >>= 1
            position <<= 1
        
        return result