class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        prefix1 = deque(s1)
        prefix2 = deque(s2)
        
        while prefix1 and prefix2 and prefix1[0]==prefix2[0]:
            prefix1.popleft()
            prefix2.popleft()
        
        while prefix1 and prefix2 and prefix1[-1]==prefix2[-1]:
            prefix1.pop()
            prefix2.pop()
        
        if not prefix1 or not prefix2:
            return True
        return False