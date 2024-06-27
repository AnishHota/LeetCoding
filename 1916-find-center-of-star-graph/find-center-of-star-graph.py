class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        for x,y in edges:
            freq[x]+=1
            freq[y]+=1
        
        n = len(freq)
        for x,y in freq.items():
            if y==n-1:
                return x
        