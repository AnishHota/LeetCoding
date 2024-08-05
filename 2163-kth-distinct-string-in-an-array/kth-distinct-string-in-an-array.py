class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        freq = sorted(freq.items(),key=lambda x: x[1])
        if k>len(freq):
            return ""
        if freq[k-1][1]==1:
            return freq[k-1][0]
        return ""
        