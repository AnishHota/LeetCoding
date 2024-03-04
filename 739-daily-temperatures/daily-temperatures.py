class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]

        stack = []
        stack.append(0)

        for i,t in enumerate(temperatures):
            if i==0:
                continue
            while stack and t>temperatures[stack[-1]]:
                ind = stack.pop()
                ans[ind] = i-ind
            stack.append(i)
        
        return ans
