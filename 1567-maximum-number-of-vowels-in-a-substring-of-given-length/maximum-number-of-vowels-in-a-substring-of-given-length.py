class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        ans = 0
        for i in range(k):
            if s[i] in vowel:
                ans += 1
        j=0
        curr = ans
        for i in range(k,len(s)):
            if s[j] in vowel:
                curr-=1
            if s[i] in vowel:
                curr+=1
            if curr>ans:
                ans = curr
            j+=1
        
        return ans
        