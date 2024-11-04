class Solution:
    def compressedString(self, word: str) -> str:
        
        count = None
        ch = None
        prev = None
        comp = ""
        for x in word:
            if not prev:
                ch = x
                count = 1
                prev = ch
            elif x==prev and count+1==9:
                comp += "9"+x
                count = 0
                prev = None
            elif x==prev:
                count+=1
            else:
                comp += str(count)+ch
                ch = x
                prev = ch
                count = 1
        if count!=0:
            comp += str(count)+x
        return comp


