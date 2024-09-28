class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        i,j = 0,len(s)-1
        st = list(s)
        while i<j:
            while i<j and st[i] not in vowels:
                i+=1
            while i<j and st[j] not in vowels:
                j-=1
            if i<j:
                st[i],st[j] = st[j],st[i]
                i+=1
                j-=1
        return ''.join(st)