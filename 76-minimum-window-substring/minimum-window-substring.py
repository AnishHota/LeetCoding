class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sdict = {}
        tdict = collections.defaultdict(int)

        for x in t:
            tdict[x]+=1
            sdict[x]=0
        have,need = 0,len(tdict)
        l=0
        ans = float('inf')
        lind,rind = -1,-1
        for r in range(len(s)):
            if s[r] in sdict:
                sdict[s[r]]+=1
                if sdict[s[r]]==tdict[s[r]]:
                    have+=1
                while l<=r and have==need:
                    if ans>(r-l+1):
                        ans = r-l+1
                        lind = l
                        rind = r
                    if s[l] in sdict:
                        sdict[s[l]]-=1
                        if sdict[s[l]]<tdict[s[l]]:
                            have-=1
                    l+=1
        return s[lind:rind+1] if lind!=-1 else ""
                        
            
        
        