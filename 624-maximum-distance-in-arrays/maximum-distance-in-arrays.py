class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxHeap = []
        minHeap = []

        for i,x in enumerate(arrays):
            heappush(minHeap,(x[0],i))
            heappush(maxHeap,(-x[-1],i))
            
        if minHeap[0][1]!=maxHeap[0][1]:
            return abs(minHeap[0][0]+maxHeap[0][0])
        else:
            a = heappop(minHeap)[0]
            b = heappop(minHeap)[0]
            p = heappop(maxHeap)[0]
            q = heappop(maxHeap)[0]
            return max(abs(a+q),abs(b+p))
            

