class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        freq = Counter(s)
        ans = ""
        ans += (freq['1']-1)*'1'
        ans += freq['0']*'0'
        return ans+"1"
        