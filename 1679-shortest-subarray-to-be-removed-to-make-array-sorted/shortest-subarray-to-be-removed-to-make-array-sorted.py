class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0,len(arr)-1

        while left<len(arr)-1 and arr[left+1]>=arr[left]:
            left+=1
        
        if left == len(arr)-1:
            return 0
        
        while right>=0 and arr[right-1]<=arr[right]:
            right-=1
        
        i,j = 0, right
        ans = min(len(arr)-left-1,right)
        while i<=left and j<len(arr):
            if arr[i]<=arr[j]:
                ans = min(ans, j-i-1)
                i+=1
            else:
                j+=1
        
        return ans

