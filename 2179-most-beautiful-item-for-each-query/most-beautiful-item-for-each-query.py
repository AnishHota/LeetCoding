class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key=lambda x: (x[0],x[1]))
        stack = [(0,0)]
        
        for p,b in items:
            if b>stack[-1][1]:
                stack.append((p,b))

        ans = [] 
        for q in queries:
            for i in range(len(stack)-1,-1,-1):
                if stack[i][0]<=q:
                    ans.append(stack[i][1])
                    break
        return ans