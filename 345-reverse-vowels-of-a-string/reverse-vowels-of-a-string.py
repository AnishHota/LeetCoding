class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vo = []
        for x in s:
            if str.lower(x) in vowels:
                vo.append(x)
        res = ""
        j = len(vo)-1
        for x in s:
            if str.lower(x) in vowels:
                res+=vo[j]
                j-=1
            else:
                res+=x
        return res