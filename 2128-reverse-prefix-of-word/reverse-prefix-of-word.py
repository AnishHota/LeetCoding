class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = -1

        for i,w in enumerate(word):
            if w==ch:
                ind = i
                break
        
        if ind==-1:
            return word
        
        return word[ind::-1]+word[ind+1:]