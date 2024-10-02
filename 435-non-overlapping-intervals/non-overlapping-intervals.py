class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x:x[1])
        stack = []
        res = 0
        for i,(s,e) in enumerate(intervals):
            if not stack:
                stack.append((s,e))
                continue
            start,end = stack[-1][0], stack[-1][1]
            if s<end and end>=s:
                if s>=start and e<end:
                    stack.pop()
                    stack.append((s,e))
                res+=1
            else:
                stack.append((s,e))   
            # print(stack)
        return res