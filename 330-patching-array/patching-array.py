class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_i = 0
        ans = 0
        i=0
        while max_i<n:
            if i<len(nums) and max_i+1>=nums[i]:
                max_i+=nums[i]
                i+=1
            else:
                ans+=1
                max_i+=max_i+1
        return ans
        