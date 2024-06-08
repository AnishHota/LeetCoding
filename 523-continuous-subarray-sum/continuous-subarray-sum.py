class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        hash = {}
        for i,x in enumerate(nums):
            num = nums[i]+prefix
            prefix = num
            mod = num%k
            if (i>=1 and mod==0) or (mod in hash and i-hash[mod]>1):
                return True
            elif mod not in hash:
                hash[mod]=i

        return False
        