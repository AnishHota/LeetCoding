class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXor = [0] + arr[:]
        for i in range(1,n+1):
            prefixXor[i] ^= prefixXor[i-1]

        ans = 0
        for i in range(len(arr)+1):
            for j in range(i+1,len(arr)+1):
                if prefixXor[i]==prefixXor[j]:
                    ans += j-i-1
        
        return ans