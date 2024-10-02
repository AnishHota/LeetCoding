class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = list(set(arr))
        heapq.heapify(heap)
        ind = {}
        count = 1

        while heap:
            n = heapq.heappop(heap)
            if n not in ind:
                ind[n]=count
                count+=1
        
        for i,x in enumerate(arr):
            arr[i] = ind[x]
        
        return arr
        