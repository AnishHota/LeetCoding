class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        score = 0
        maxS = 0
        if tokens and power>=tokens[0]:
            score+=1
            maxS+=1
            power = power - tokens[0]
        else:
            return 0
        
        l,r = 1,len(tokens)-1
        while l<=r:
            if power>=tokens[l]:
                score+=1
                maxS = max(score,maxS)
                power-=tokens[l]
                l+=1
            elif score>0:
                score-=1
                power+=tokens[r]
                r-=1
            else:
                return maxS
        
        return maxS


        