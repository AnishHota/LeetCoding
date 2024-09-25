class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix = defaultdict(int)
        for w in words:
            for i in range(1,len(w)+1):
                prefix[w[:i]]+=1

        res = []
        for w in words:
            temp = 0
            for i in range(1,len(w)+1):
                temp += prefix[w[:i]]
            res.append(temp)
        
        return res