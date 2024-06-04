class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for x in freq.values():
            if x%2==0:
                ans +=x
            else:
                ans += x-1
        if ans == sum(freq.values()):
            return ans
        return ans+1