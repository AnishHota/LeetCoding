class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            if x>0 or not stack or stack[-1]<0:
                stack.append(x)
            else:
                while stack:
                    if stack[-1]<0:
                        stack.append(x)
                        break
                    elif stack[-1]==abs(x):
                        stack.pop()
                        break
                    elif stack[-1]<abs(x):
                        stack.pop()
                        if not stack:
                            stack.append(x)
                            break
                    else:
                        break
        
        return stack