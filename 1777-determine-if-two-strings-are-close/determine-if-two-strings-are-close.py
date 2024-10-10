class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)

        if len(f1.keys()-f2.keys())>0 or len(f2.keys()-f1.keys())>0:
            return False

        cnt1 = list(f1.values())
        cnt2 = list(f2.values())
        cnt1.sort()
        cnt2.sort()
        return cnt1==cnt2