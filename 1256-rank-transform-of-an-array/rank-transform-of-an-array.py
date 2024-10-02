class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        ind = {}
        x = sorted(set(arr))
        for i,c in enumerate(x):
            ind[c]=i+1
        
        for i,a in enumerate(arr):
            arr[i] = ind[a]
        
        return arr
        