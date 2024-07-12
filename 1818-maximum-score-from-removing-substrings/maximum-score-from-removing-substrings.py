class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        gain = 0
        if x>y:
            stack = []
            for c in s:
                if c=='b' and stack and stack[-1]=='a':
                    gain += x
                    stack.pop()
                else:
                    stack.append(c)
            if stack:
                new_stack = []
                for c in stack:
                    if c=='a' and new_stack and new_stack[-1]=='b':
                        gain+=y
                        new_stack.pop()
                    else:
                        new_stack.append(c)
        else:
            stack = []
            for c in s:
                if c=='a' and stack and stack[-1]=='b':
                    gain += y
                    stack.pop()
                else:
                    stack.append(c)
            if stack:
                new_stack = []
                for c in stack:
                    if c=='b' and new_stack and new_stack[-1]=='a':
                        gain+=x
                        new_stack.pop()
                    else:
                        new_stack.append(c)

        return gain

