class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt = 0
        for x in s:
            if x=='1':
                cnt += 1
            else:
                ans += cnt

        return ans