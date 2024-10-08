class Solution:
    def minSwaps(self, s: str) -> int:
        q = list(s)
        cnto=0
        cntc=0
        j = len(s)-1
        while j>=0 and q[j]!='[':
            j-=1
        res=0

        for i,x in enumerate(q):
            if x=='[':
                cnto+=1
            if x==']':
                cntc+=1
            if cntc>cnto and i<j:
                    q[i],q[j]=q[j],q[i]
                    cntc-=1
                    cnto+=1
                    res+=1
                    while j>=0 and q[j]!='[':
                        j-=1

        return res