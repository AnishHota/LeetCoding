class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position,speed),reverse=True)
        ans = 0
        flag = 0
        for x,y in arr:
            dist = (target-x)/y

            if dist>flag:
                flag = dist
                ans+=1
                
        return ans
        