class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                    ind, height = stack.pop()
                    maxA = max(maxA, height*(i-ind))
                    start = ind
            stack.append((start,h))
        
        for i,h in stack:
            maxA = max(maxA, h*(len(heights)-i))
        
        return maxA