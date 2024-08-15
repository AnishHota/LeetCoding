class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills5,bills10 = 0,0
        for x in bills:
            if x==5:
                bills5 += 1
            if x==10:
                if bills5>0:
                    bills5-=1
                    bills10+=1
                else:
                    return False
            if x==20:
                if (bills5>=3 or (bills5>0 and bills10>0)):
                    if bills10>0:
                        bills10-=1
                        bills5-=1
                    else:
                        bills5-=3
                else:
                    return False
        return True