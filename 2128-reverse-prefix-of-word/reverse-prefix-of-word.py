class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for i,w in enumerate(word):
            if w==ch:
                return word[i::-1]+word[i+1:]
        return word
        
        