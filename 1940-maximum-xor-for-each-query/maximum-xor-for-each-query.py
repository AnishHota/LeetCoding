class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        curr = 0
        n = 2**maximumBit - 1
        ans = []
        for x in nums:
            curr = curr ^ x
            ans.append(curr ^ n)
        
        return ans[::-1]