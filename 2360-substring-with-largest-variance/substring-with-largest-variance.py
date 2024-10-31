class Solution:
    def largestVariance(self, s: str) -> int:
        
        s1 = set(s)
        s2 = set(s)

        pairs = [(l1,l2) for l1 in s1 for l2 in s2 if l1!=l2]
        var = 0
        ans = 0
        for _ in range(2):
            for p in pairs:
                c1 = c2 = 0
                l1,l2 = p
                for x in s:
                    if x!=l1 and x!=l2:
                        continue
                    if x==l1:
                        c1+=1
                    elif x==l2:
                        c2+=1
                    if c1<c2:
                        c1=c2=0
                    elif c1>0 and c2>0:
                        ans = max(ans, c1-c2)
            s = s[::-1]
        
        return ans

