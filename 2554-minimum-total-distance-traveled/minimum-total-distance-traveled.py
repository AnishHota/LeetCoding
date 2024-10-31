class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        factory = sorted(factory, key=lambda x: x[0])
        robot = sorted(robot)
        memo = {}
        def helper(curR, curF, usedC):
            if curR == len(robot):
                return 0
            if curF == len(factory):
                return float('inf')
            
            key = (curR, curF, usedC)
            if key in memo:
                return memo[key]
            
            minDist = helper(curR, curF+1,0)
            pos, cap = factory[curF]
            if usedC<cap:
                dist = abs(pos-robot[curR])
                minDist = min(minDist,dist+helper(curR+1, curF, usedC+1))
            
            memo[key]=minDist
            return minDist
        
        return helper(0,0,0)
        