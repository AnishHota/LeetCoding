class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if len(s1)==len(s2):
            return Counter(s1)==Counter(s2)
        
        freq = Counter(s1)
        cnt = 0
        tot = len(freq)
        n = len(s1)

        for j in range(len(s2)):
            if s2[j] in freq:
                if freq[s2[j]]==0:
                    cnt-=1
                
                freq[s2[j]]-=1

                if freq[s2[j]]==0:
                    cnt+=1
                

            if j>=n and s2[j-n] in freq:
                if freq[s2[j-n]]==0:
                    cnt-=1

                freq[s2[j-n]]+=1
                
                if freq[s2[j-n]]==0:
                    cnt+=1

            if cnt==tot:
                return True  

        return False