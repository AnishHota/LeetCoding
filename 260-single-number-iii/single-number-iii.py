class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorall = 0
        for x in nums:
            xorall ^= x

        bit = xorall & -xorall
        xor_a = 0
        xor_b = 0
        for x in nums:
            if x & bit:
                xor_a ^= x
            else:
                xor_b ^= x
        
        return [xor_a,xor_b]