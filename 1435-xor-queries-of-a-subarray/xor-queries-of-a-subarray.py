class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = [arr[0]]
        n = len(arr)
        for i in range(1,n):
            prexor.append(prexor[-1]^arr[i])

        ans = []
        for x,y in queries:
            temp = prexor[y]
            if x>0:
                temp = temp ^ prexor[x-1]
            ans.append(temp)
        return ans