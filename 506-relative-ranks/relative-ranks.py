class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreSort = sorted(score,reverse=True)
        hash = {}
        for i,x in enumerate(scoreSort):
            if i==0:
                hash[x]="Gold Medal"
            elif i==1:
                hash[x]="Silver Medal"
            elif i==2:
                hash[x]="Bronze Medal"
            else:
                hash[x]=str(i+1)
        ans = []
        for x in score:
            ans.append(hash[x])
        
        return ans
            