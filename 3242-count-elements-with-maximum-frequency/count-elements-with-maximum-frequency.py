from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0 for _ in range(101)]
        maxFreq = 0
        elems = 0
        for x in nums:
            freq[x]+=1
            if freq[x]>maxFreq:
                maxFreq = freq[x]
                elems=1
            elif freq[x]==maxFreq:
                elems+=1
        
        return elems*maxFreq
