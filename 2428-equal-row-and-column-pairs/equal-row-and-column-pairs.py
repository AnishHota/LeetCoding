class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        colhash = defaultdict(int)
        rowhash = defaultdict(int)
        colset = set()
        rowset = set()
        r,c = len(grid), len(grid[0])
        for i in range(r):
            row = '#'.join(map(str,grid[i]))
            rowhash[row]+=1
            rowset.add(row)
        
        for j in range(c):
            col = []
            for i in range(r):
                col.append(str(grid[i][j]))
            col = '#'.join(col)
            colhash[col]+=1
            colset.add(col)
        
        res = 0
        for x in rowset.intersection(colset):
            res += rowhash[x]*colhash[x]
        
        return res