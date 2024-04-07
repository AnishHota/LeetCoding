class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0,0
        for x in s:
            if x==")":
                leftMax-=1
                leftMin-=1
                if leftMax<0:
                    return False
            if x=="(":
                leftMax+=1
                leftMin+=1
            if x=="*":
                leftMin-=1
                leftMax+=1
            leftMin = max(0,leftMin)

        return leftMin==0