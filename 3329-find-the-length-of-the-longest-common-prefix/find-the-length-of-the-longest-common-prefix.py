class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()

        for a in arr1:
            x = str(a)
            pre = ""
            for ch in x:
                pre += ch
                prefix.add(pre)
        
        ans = 0
        for a in arr2:
            x = str(a)
            pre = ""
            for j in range(len(x),-1,-1):
                if x[:j] in prefix:
                    ans = max(ans,j)
                    break

        return ans