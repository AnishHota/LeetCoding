class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        ans = []
        for x in arr2:
            ans+=[x]*freq[x]
            freq[x]=0
        
        freq = sorted(freq.items())
        for k,v in freq:
            if v!=0:
                ans+=[k]*v
        return ans

