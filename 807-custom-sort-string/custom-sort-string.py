class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0 for _ in range(26)]
        ans =""
        for x in s:
            freq[ord(x)-ord('a')]+=1
        
        for x in order:
            if freq[ord(x)-ord('a')]!=0:
                ans+=x*freq[ord(x)-ord('a')]
                freq[ord(x)-ord('a')]=0
        
        for i,x in enumerate(freq):
            if x!=0:
                ans+=chr(i+ord('a'))*freq[i]
        
        return ans