class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            n = len(arr)
            if n==1:
                return arr
            larr, rarr = merge(arr[:n//2]), merge(arr[n//2:])
            return mergesort(larr,rarr)
        
        def mergesort(larr,rarr):
            i,j = 0,0
            res = []
            while i<len(larr) and j<len(rarr):
                if larr[i]<=rarr[j]:
                    res.append(larr[i])
                    i+=1
                else:
                    res.append(rarr[j])
                    j+=1
            if i<len(larr):
                res += larr[i:]
            elif j<len(rarr):
                res += rarr[j:]
            return res
        
        return merge(nums)
                
