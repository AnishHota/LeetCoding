class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        j1,j2 = len(s1)-1, len(s2)-1
        i=0
        while i<len(s1) and i<len(s2):
            if s1[i]==s2[i]:
                i += 1
            elif s1[j1]==s2[j2]:
                j1-=1
                j2-=1
            else:
                break

        if i>j1 or i>j2:
            return True
        return False