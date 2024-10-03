class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefix = 0
        dic = {0:-1}
        target = sum(nums)%p
        res = float('inf')
        if target==0:
            return 0
        for i in range(n):
            prefix = (prefix+nums[i])%p
            if (prefix-target)%p in dic:
                res = min(res,i-dic[(prefix-target)%p])
            dic[prefix]=i
        
        if res>=n:
            return -1
        return res