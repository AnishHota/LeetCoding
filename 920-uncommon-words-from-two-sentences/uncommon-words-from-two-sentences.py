class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = set()
        s1count = Counter(s1.split(" "))
        s2count = Counter(s2.split(" "))
        for k,v in s1count.items():
            if v==1 and k not in s2count:
                ans.add(k)
        
        for k,v in s2count.items():
            if v==1 and k not in s1count:
                ans.add(k)
        
        return ans

