from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        track = defaultdict(list)
        r, c = 9,9
        for i in range(r):
            for j in range(c):
                if board[i][j]!=".":
                    print(board[i][j])
                    if track[board[i][j]]:
                        if (i in track[board[i][j]][0]) or (j in track[board[i][j]][1]):
                            # print(board[i][j])
                            # print(i,track[board[i][j]][0])
                            # print(j,track[board[i][j]][1])
                            return False
                        if int(int((i/3))*3+int(j/3)) in track[board[i][j]][2]:
                            # print(board[i][j],i,j)
                            # print(int(int((i/3))*3+int(j/3)),track[board[i][j]][2])
                            return False
                        track[board[i][j]][0].append(i)
                        track[board[i][j]][1].append(j)
                        track[board[i][j]][2].append(int(int((i/3))*3+int(j/3)))
                    else:
                        track[board[i][j]] = [[i],[j],[int(int((i/3))*3+int(j/3))]]
        
        return True