class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched = 0
        count = 0
        for x in s:
            if x=='(':
                unmatched +=1
            elif unmatched>0:
                unmatched -=1
            else:
                count+=1
        
        return unmatched+count