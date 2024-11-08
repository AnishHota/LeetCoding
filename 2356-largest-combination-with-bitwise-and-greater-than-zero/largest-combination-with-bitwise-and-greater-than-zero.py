class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for candidate in candidates:
                if candidate & (1<<i):
                    cnt += 1
            ans = max(cnt, ans)
        
        return ans