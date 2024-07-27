class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        arr = [[float('inf') for _ in range(26)] for _ in range(26)]

        for i in range(26):
            arr[i][i] = 0

        for o,c,cos in zip(original,changed,cost):
            ind_o = ord(o)-ord('a')
            ind_c = ord(c)-ord('a')
            arr[ind_o][ind_c] = min(arr[ind_o][ind_c],cos)
        
        ans = 0

        for middle in range(26):
            for i in range(26):
                for j in range(26):
                    arr[i][j] = min(arr[i][j],arr[i][middle]+arr[middle][j])
        
        for i in range(len(source)):
            if source[i]!=target[i]:
                ind_s = ord(source[i])-ord('a')
                ind_t = ord(target[i])-ord('a')
                if arr[ind_s][ind_t]==float('inf'):
                    return -1
                ans += arr[ind_s][ind_t]
        
        return ans
