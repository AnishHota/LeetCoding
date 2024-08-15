class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = 0
        bills5,bills10 = 0,0
        for x in bills:
            if x==5:
                money+=x
                bills5 += 1
            elif money>=(x-5):
                change = x-5
                while bills10>0 and change>=10:
                    change-=10
                    bills10-=1
                while bills5>0 and change>=5:
                    change-=5
                    bills5-=1
                if change!=0:
                    return False
                money+=5
                if x==10:
                    bills10+=1
            else:
                return False
        return True