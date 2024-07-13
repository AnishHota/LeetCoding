class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = []
        phd = sorted(zip(positions,healths,directions))
        stack = []
        for p,h,d in phd:
            if d=='L' and stack:
                add = True
                while stack and stack[-1][2]=='R' and add:
                    if h>stack[-1][1]:
                        stack.pop()
                        h-=1
                    elif h<stack[-1][1]:
                        stack[-1][1]-=1
                        add = False
                        break
                    else:
                        stack.pop()
                        add = False
                        break
                if add:
                    stack.append([p,h,d])
            else:
                stack.append([p,h,d])

        order_dict = {value: index for index, value in enumerate(positions)}
        sorted_arr = sorted(stack, key=lambda x: order_dict[x[0]])
        ans = [x[1] for x in sorted_arr]

        return ans