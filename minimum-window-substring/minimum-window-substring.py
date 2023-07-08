class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        strt,end = 0,0
        b = Counter(t)
        target_len=len(t)
        minLen = sys.maxsize
        for j in range(len(s)):
    
            if b[s[j]]>0:
                target_len -= 1

            b[s[j]]-=1

            while target_len==0: 
                if (j-i+1)<minLen:
                    minLen = j-i+1
                    strt = i
                    end = j+1

                b[s[i]]+=1

                if b[s[i]]>0:
                    target_len+=1
                i+=1
    
                
        return s[strt:end]
        

                    