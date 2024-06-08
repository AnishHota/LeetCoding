class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        hash = {}
        for i,x in enumerate(nums):
            num = nums[i]+prefix[i]
            prefix.append(num)
            mod = num%k
            if (mod in hash and abs(hash[mod]-i)>=2) or (i>=1 and mod==0):
                return True
            elif mod not in hash:
                hash[mod]=i

        return False
        