class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans= ""
        nums = sorted(nums, key=lambda x:x/(10**len(str(x))-1),reverse=True)
        nums = [str(n) for n in nums]
        return str(int(''.join(nums)))
