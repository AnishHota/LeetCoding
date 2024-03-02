class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        ans = 0
        le = 0
        for x in s:
            if x-1 not in s:
                le=1
                while x+1 in s:
                    x=x+1
                    le+=1
                ans = max(le,ans)

        return ans
