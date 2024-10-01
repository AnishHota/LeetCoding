class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for x in arr:
            freq[((x%k)+k)%k]+=1
        count = 0
        for i in range(k):
            if i==0 or i==k-i:
                if freq[i]%2!=0:
                    return False
                count+=freq[i]
            elif freq[i]!=freq[k-i]:
                return False
            else:
                count += freq[i]
        if count==len(arr):
            return True
        return False