class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                cur_val,cur_i = stack.pop()
                ans[cur_i]=i-cur_i
            stack.append((temp,i))
        
        return ans

        