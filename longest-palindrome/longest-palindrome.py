class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        dic = Counter(s)
        for x in dic:
            if dic[x]%2==0:
                l+=dic[x]
                dic[x]=0
            elif dic[x]>2:
                l+=dic[x]-1
                dic[x]=1
        
        for x in dic:
            if dic[x]==1:
                l += 1
                break
        return l