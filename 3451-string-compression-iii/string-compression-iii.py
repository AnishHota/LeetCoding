class Solution:
    def compressedString(self, word: str) -> str:
        
        count = 1
        ch = word[0]
        comp = ""
        for x in word[1:]:
            if x==ch:
                count+=1
                if count==10:
                    comp+="9"+ch
                    count = 1
            else:
                comp += str(count)+ch
                count = 1
                ch = x

        comp += str(count)+ch
        return comp


