class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        dic = Counter(s)
        for x in dic:
            if dic[x]%2!=0:
                l+=1
        return len(s)-l+bool(l)
    