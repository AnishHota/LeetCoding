class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [1] * (n+1)
        arr[0] = 0 
        count = n-1
        temp_k = k
        i = 1
        while count!=0:
            if arr[i]==1:
                temp_k-=1
            if temp_k==0:
                arr[i]=0
                count-=1 
                temp_k = k
            i+=1
            if i>n:
                i = 0
        
        for i,x in enumerate(arr):
            if x==1:
                return i
            
