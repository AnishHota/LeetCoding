class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        m = []

        for tp in timePoints:
            h,mi = map(int,tp.split(":"))
            m.append(h*60+mi)
        m.sort()
        small = float("inf")
        for i in range(len(m)-1):
            if m[i+1]-m[i]<small:
                small = m[i+1]-m[i]
        
        if 24*60-m[-1]+m[0]<small:
            small = 24*60-m[-1]+m[0]
        
        return small

