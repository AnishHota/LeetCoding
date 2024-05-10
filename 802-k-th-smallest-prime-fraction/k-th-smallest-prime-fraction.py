class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        frac = {}
        for i in range(n):
            for j in range(i+1,n):
                frac[(arr[i],arr[j])] = float(arr[i]/arr[j])
        
        frac = sorted(frac.items(), key=lambda x:x[1])
        return list(frac[k-1][0])