class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = [arr[0]]
        sufxor = [arr[-1]]
        n = len(arr)
        for i in range(1,n):
            prexor.append(prexor[-1]^arr[i])
            sufxor.append(sufxor[-1]^arr[n-i-1])
        sufxor = sufxor[::-1]
        total = prexor[-1]
        ans = []
        for x,y in queries:
            temp = total
            if x>0:
                temp = temp ^ prexor[x-1]
            if y<len(arr)-1:
                temp = temp ^ sufxor[y+1]
            ans.append(temp)
        return ans