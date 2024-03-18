class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        ans = []
        ans.append(points[0])
        for i in range(len(points)):
            if ans[-1][1]>=points[i][0]:
                temp = ans.pop()
                ans.append([max(temp[0],points[i][0]),min(temp[1],points[i][1])])
            else:
                ans.append(points[i])
        return len(ans)

        