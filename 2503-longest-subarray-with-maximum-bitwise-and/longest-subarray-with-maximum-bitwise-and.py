class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        large = max(nums)
        ans = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i]==large:
                curr += 1
                ans = max(curr,ans)
            else:
                curr = 0
        return ans
            