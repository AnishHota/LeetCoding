class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        freq = defaultdict(int)

        for x in hand:
            freq[x]+=1
        
        freq = dict(sorted(freq.items(), key=lambda x:x[0]))
        for k in freq.keys():
            while freq[k]!=0:
                j=0
                while j!=groupSize:
                    if (k+j) not in freq or freq[k+j]==0:
                        return False
                    freq[k+j]-=1
                    j+=1
        
        return True



