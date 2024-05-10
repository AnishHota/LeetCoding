class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        left, right = 0,1
        n = len(arr)
        
        while left<=right:
            mid = (left+right)/2
            total_small = 0
            ansi, ansj = 0,0
            max_fraction=0.0
            j=1
            for i in range(n-1):
                while j<n and arr[i]/arr[j]>=mid:
                    j+=1
                
                total_small += n-j
                if j==n:
                    break
                fraction = arr[i]/arr[j]
                if fraction>max_fraction:
                    max_fraction = fraction
                    ansi = i
                    ansj = j
            
            if total_small==k:
                return [arr[ansi],arr[ansj]]
            elif total_small>k:
                right = mid
            else:
                left = mid
        
        return []
            
                
    