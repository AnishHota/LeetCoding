class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        for row in box:
            dropPos = len(row)-1
            for currPos in range(len(row)-1,-1,-1):
                if row[currPos] == "*":
                    dropPos = currPos - 1
                elif row[currPos] == "#":
                    row[currPos], row[dropPos] = row[dropPos], row[currPos]
                    dropPos -=1

        return zip(*box[::-1])
