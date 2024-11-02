class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)-1):
            if words[i][-1]!=words[i+1][0]:
                return False
        
        if words[-1][-1]==words[0][0]:
            return True
        
        return False