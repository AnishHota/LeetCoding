class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)

        if k>=tot:
            k = k%tot
        
        for i,ch in enumerate(chalk):
            if ch>k:
                return i
            k-=ch
