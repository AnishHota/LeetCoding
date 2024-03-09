class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sdict = collections.defaultdict(int)
        for x in s1:
            sdict[x]+=1
        
        bdict = collections.defaultdict(int)
        count=0
        l,r = 0,0
        while r<len(s2):
            while r<len(s2) and (r-l)!=len(s1):
                bdict[s2[r]]+=1
                if s2[r] in sdict and bdict[s2[r]]<=sdict[s2[r]]:
                    count+=1
                r+=1
            if count==len(s1):
                    return True
            if s2[l] in sdict and bdict[s2[l]]<=sdict[s2[l]]:
                count-=1
            bdict[s2[l]]-=1
            l+=1
            
        return False
            
            
