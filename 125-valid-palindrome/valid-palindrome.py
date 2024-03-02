class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                newS+=c
        
        return newS==newS[::-1]
        