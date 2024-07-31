class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        minHeight = [float('inf')]*(n+1)
        minHeight[0] = 0

        for i in range(1,n+1):
            currHeight = 0
            currWidth = 0
            for j in range(i-1,-1,-1):
                if currWidth+books[j][0]>shelfWidth:
                    break
                
                currHeight = max(books[j][1],currHeight)
                currWidth+=books[j][0]
                minHeight[i] = min(currHeight+minHeight[j], minHeight[i])

        return minHeight[n]