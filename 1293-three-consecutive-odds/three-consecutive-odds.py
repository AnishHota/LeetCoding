class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        cnt = 0
        for x in arr:
            if x%2!=0:
                cnt+=1
            else:
                cnt=0
            if cnt==3:
                return True
        
        return False