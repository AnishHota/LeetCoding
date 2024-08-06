class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        freq = sorted(freq.items(),key=lambda x:-x[1])
        ans = 0
        first,second,third,fourth = 0,0,0,0
        for i,(ch,cnt) in enumerate(freq):
            if i<8:
                first += cnt
            elif i<16:
                second += cnt
            elif i<24:
                third += cnt
            else:
                fourth += cnt
        ans = first*1 + second*2 + third*3 + fourth*4
        return ans