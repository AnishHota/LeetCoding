class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = [(capital[i],profits[i]) for i in range(len(profits))]
        proj.sort()
        heap = []
        j = 0
        for i in range(k):

            while j<len(proj) and w>=proj[j][0]:
                heapq.heappush(heap, -proj[j][1])
                j+=1
            
            if not heap:
                break
            
            w -= heapq.heappop(heap)
        
        return w
            
