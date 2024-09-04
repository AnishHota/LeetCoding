class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        ind_dir = 0
        x,y = 0,0
        ans = 0
        obs = set()
        for a,b in obstacles:
            obs.add((a,b))
        for c in commands:
            if c==-1:
                ind_dir = (ind_dir+1)%4
            elif c==-2:
                ind_dir = (ind_dir-1)%4
            else:
                for _ in range(c):
                    change_x,change_y = d[ind_dir]
                    if (x+change_x,y+change_y) in obs:
                        break
                    x += change_x
                    y += change_y
                    ans = max(ans, x**2 + y**2)
        return ans