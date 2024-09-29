class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j = 0,0
        while i<len(chars):
            count = 1
            chars[j] = chars[i]
            while i+1<len(chars) and chars[i+1]==chars[j]:
                i+=1
                count+=1
            if count!=1:
                for x in str(count):
                    chars[j+1]=x
                    j+=1
            i+=1
            j+=1
        
        return j

        