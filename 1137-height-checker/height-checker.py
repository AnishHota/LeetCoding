class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_sort = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i]!=height_sort[i]:
                ans+=1
        return ans