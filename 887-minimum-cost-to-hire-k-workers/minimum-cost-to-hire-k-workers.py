class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        pairs = []

        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i],quality[i]))
        
        pairs.sort(key=lambda x:x[0])

        total_quality = 0
        maxHeap = []
        res = float("inf")
        for rate,q in pairs:
            total_quality += q
            heappush(maxHeap,-q)

            if len(maxHeap)>k:
                total_quality += heappop(maxHeap)
            
            if len(maxHeap)==k:
                res = min(res, total_quality*rate)
        
        return res