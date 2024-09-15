class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bits = {0:-1}
        vowels = ['a','e','i','o','u']
        ans = 0
        curr = 0
        for i,c in enumerate(s):
            if c in vowels:
                curr = curr ^ ord(c)
            if curr in bits:
                ans = max(ans,i-bits[curr])
            else:
                bits[curr]=i
        return ans