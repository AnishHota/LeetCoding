class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(map(int,list(s)))
        i = 0
        n = len(arr)
        while i<n and arr[i]==0:
            i+=1
        
        ans = 0
        for j in range(i,n):
            if arr[j]==0:
                arr[i],arr[j] = arr[j],arr[i]
                ans += j-i
                i+=1

        return ans