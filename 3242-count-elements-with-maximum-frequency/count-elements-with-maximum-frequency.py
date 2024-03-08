from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxFreq = 0
        elems = 0
        for x in freq:
            if freq[x]>maxFreq:
                maxFreq = freq[x]
                elems=1
            elif freq[x]==maxFreq:
                elems+=1
        
        return elems*maxFreq
