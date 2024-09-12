class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        als = 0
        for a in allowed:
            als |= 1<<(ord(a)-ord('a'))
        
        count = 0
        for w in words:
            for c in w:
                temp = 1<<(ord(c)-ord('a'))
                if temp&als==0:
                    count+=1
                    break
        
        return len(words)-count