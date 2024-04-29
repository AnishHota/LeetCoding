class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        xor = 0
        for x in nums:
            xor ^= x 
        
        ans = xor^k
        return bin(ans).count("1")