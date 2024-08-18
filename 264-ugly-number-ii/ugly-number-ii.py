class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        
        arr = [0]*(n)
        arr[0]=1
        a,b,c = 0,0,0

        for i in range(1,n):
            arr[i] = min(arr[a]*2,arr[b]*3,arr[c]*5)
            if arr[i]==arr[a]*2:
                a+=1
            if arr[i]==arr[b]*3:
                b+=1
            if arr[i]==arr[c]*5:
                c+=1
        
        return arr[n-1]