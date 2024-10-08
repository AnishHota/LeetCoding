class Solution:
    def minSwaps(self, s: str) -> int:
        cnto=0
        cntc=0
        j = len(s)-1
        while j>=0 and s[j]!='[':
            j-=1
        res=0
        if not s:
            return res
        if j<len(s)//2:
            return res

        for i,x in enumerate(s):
            if x=='[':
                cnto+=1
            elif x==']':
                cntc+=1
            if cntc>cnto and i<j:
                    cntc-=1
                    cnto+=1
                    res+=1
                    j-=1
                    while j>=0 and s[j]!='[':
                        j-=1

        return res