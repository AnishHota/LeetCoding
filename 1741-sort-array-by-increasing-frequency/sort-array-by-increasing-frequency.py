class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for n,f in sorted(freq.items(),key=lambda x: (x[1],-x[0])):
            ans += [n]*f
        return ans